import base64
import io
import json
import logging
import tempfile

import anthropic
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from PIL import Image

from constants import SEASONAL_COLORS, SYSTEM_PROMPT, Seasons
from image_utils import (
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
        system="You are an expert on seasonal color analysis. Provide only the determined season name from these options: Light Spring, Warm Spring, Bright Spring, Light Summer, Cool Summer, Soft Summer, Soft Autumn, Warm Autumn, Deep Autumn, Deep Winter, Cool Winter.",
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
                        "text": "Analyze the color season of the person in this image. Provide only the determined season name.",
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
                    "text": f"The person's color season is {season}. Provide a detailed skin tone analysis, recommend a complementary color palette, and list colors to avoid. Respond in JSON format.",
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

    message = follow_up_response.content[0].text

    def extract_json(response):
        json_start = response.index("{")
        json_end = response.rfind("}")
        return json.loads(response[json_start : json_end + 1])

    return extract_json(message)
