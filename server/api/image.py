import base64
import re
import io
import json
import logging
import tempfile

import anthropic
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from PIL import Image

from constants import SEASONAL_COLORS, SYSTEM_PROMPT, Seasons
from api.image_utils import (
    MultipleFacesError,
    NoFacesError,
    get_face,
    get_padded_facial_area,
)

_ = load_dotenv()
bp = Blueprint("image_api", __name__, url_prefix="/image")


@bp.route("/", methods=["POST"])
def get_facial_area_from_image():
    """
    Get the facial area from the uploaded image.

    Returns:
        JSON: A JSON response containing the cropped image.
    """

    file = request.files.get("image")
    if not file or file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        with tempfile.NamedTemporaryFile(suffix=".jpeg") as temp_file:
            file.save(temp_file.name)
            original_img, (width, height) = (
                Image.open(temp_file.name),
                Image.open(temp_file.name).size,
            )

            _, facial_area = get_face(temp_file.name)

            cropped_img = original_img.crop(
                get_padded_facial_area(facial_area, width, height)
            )
            cropped_img_bytes = io.BytesIO()
            cropped_img.save(cropped_img_bytes, format="JPEG")
            cropped_img_base64 = base64.b64encode(cropped_img_bytes.getvalue()).decode(
                "utf-8"
            )

            analysis = get_analysis(cropped_img_base64)

            return jsonify(
                {
                    "cropped_image": cropped_img_base64,
                    "analysis": analysis,
                }
            )

    except NoFacesError:
        return (
            jsonify(
                {
                    "error": "No face detected in the image. Please upload an image with a clearly visible face in natural lighting."
                }
            ),
            400,
        )
    except MultipleFacesError:
        return (
            jsonify(
                {
                    "error": "Multiple faces detected in the image. Please upload an image with only one face."
                }
            ),
            400,
        )
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({"error": "Unexpected error occurred."}), 500


def get_season(cropped_img_base64: str):
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4,
        temperature=0,
        system="You are an expert on seasonal color analysis, with deep knowledge of the Munsell color system and its application to human coloring. You understand how to assess skin undertones (cool, warm, neutral), value (light to dark), and chroma (clear/bright vs. soft/muted). You can accurately evaluate these factors in facial images to determine seasonal color classification. Your analysis considers the interplay of skin, hair, and eye color, as well as overall contrast levels. You're familiar with the nuances that distinguish the 12 seasonal subtypes and can confidently classify individuals based on their unique combination of hue, value, and chroma characteristics.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": cropped_img_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Analyze the color season of the person in this image. Determine the single most likely season from these options: Light Spring, Warm Spring, Bright Spring, Light Summer, Cool Summer, Soft Summer, Soft Autumn, Warm Autumn, Deep Autumn, Deep Winter, Cool Winter, Bright Winter. Provide only the determined season name, with no additional explanation or commentary.",
                    },
                ],
            },
        ],
    )

    for content in response.content:
        if content.type == "text":
            return content.text


def get_analysis(cropped_img_base64: str):
    season = get_season(cropped_img_base64)

    if not season:
        return json.dumps({"error": "Could not determine season"})

    try:
        # Get the first two words of the season
        season = " ".join(season.split()[:2])
        season_enum = Seasons(season)
        tool_result = SEASONAL_COLORS[season_enum]
    except (ValueError, KeyError):
        return json.dumps({"error": f"Invalid or unsupported season: {season}"})

    client = anthropic.Anthropic()
    get_seasonal_colors_tool = {
        "name": "get_seasonal_colors",
        "description": "Get the suggested color palette and description based on the user's determined color season.",
        "input_schema": {
            "type": "object",
            "properties": {
                "season": {
                    "type": "string",
                    "enum": [season.value for season in Seasons],
                    "description": "The determined season of the user's skin tone.",
                },
            },
            "required": ["season"],
        },
    }

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": cropped_img_base64,
                    },
                },
                {
                    "type": "text",
                    "text": f'The person\'s color season is {season}. Analyze the provided image for seasonal color typing using the provided seasonal colors information. Respond in JSON format with keys:"characteristics": Key features of person\'s coloring\n,"colorsToSuggest"(list): List of dicts with "name" and "hex_code" for 12 complementary colors\n"reasonToSuggest": Why these colors complement the person\n"colorsToAvoid"(list): List of dicts with "name" and "hex_code" for 12 unflattering colors (exclude uncommon clothing colors or extremely saturated hues)\n"reasonToAvoid": Why these colors clash with the person\n"content": <50 words explanation of season determination, starting with "Based on the image provided, you have..."',
                },
            ],
        },
    ]

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system=SYSTEM_PROMPT,
        tools=[get_seasonal_colors_tool],
        tool_choice={"type": "tool", "name": "get_seasonal_colors"},
        messages=messages,
    )

    messages.append({"role": "assistant", "content": response.content})

    tool_use = response.content[-1]
    tool_name = tool_use.name
    if tool_name == "get_seasonal_colors":
        tool_response = {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(tool_result),
                }
            ],
        }
        messages.append(tool_response)

    follow_up_response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system=SYSTEM_PROMPT,
        messages=messages,
        tools=[get_seasonal_colors_tool],
    )

    message = str(follow_up_response.content[0].text)
    print(message)

    def extract_json(response):
        # Find the first occurrence of '{' and the last occurrence of '}'
        json_start = response.find("{")
        json_end = response.rfind("}")

        if json_start == -1 or json_end == -1:
            raise ValueError("No valid JSON object found in the response")

        # Extract the potential JSON string
        json_str = response[json_start : json_end + 1]

        # Remove any invalid control characters
        json_str = re.sub(r"[\x00-\x1F\x7F-\x9F]", "", json_str)

        # Try to parse the cleaned JSON string
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Problematic JSON string: {json_str}")
            raise

    try:
        extracted_json = extract_json(message)
        extracted_json["season"] = season
        return extracted_json
    except json.JSONDecodeError as e:
        print(f"Error extracting JSON: {e}")
        return json.dumps({"error": "Failed to extract valid JSON from the response"})
    except Exception as e:
        print(f"Unexpected error: {e}")
        return json.dumps({"error": f"An unexpected error occurred: {str(e)}"})
