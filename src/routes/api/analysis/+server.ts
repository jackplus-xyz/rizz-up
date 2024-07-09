import { ANTHROPIC_API_KEY } from "$env/static/private";
import type { RequestHandler } from "@sveltejs/kit";
import Anthropic from "@anthropic-ai/sdk";
import { seasonsData } from "$lib/data/seasonsData";
import { Seasons } from "$lib/types/seasons";

const anthropic = new Anthropic({ apiKey: ANTHROPIC_API_KEY });
const SYSTEM_PROMPT = `You are an expert on seasonal color analysis, with deep knowledge of the Munsell color system and its application to human coloring. You understand how to assess skin undertones (cool, warm, neutral), value (light to dark), and chroma (clear/bright vs. soft/muted). You can accurately evaluate these factors in facial images to determine seasonal color classification. Your analysis considers the interplay of skin, hair, and eye color, as well as overall contrast levels. You're familiar with the nuances that distinguish the 12 seasonal subtypes and can confidently classify individuals based on their unique combination of hue, value, and chroma characteristics.`;

async function getSeason(cropped_img_base64: string): Promise<string> {
  const response = await anthropic.messages.create({
    model: "claude-3-5-sonnet-20240620",
    max_tokens: 4,
    temperature: 0,
    system: SYSTEM_PROMPT,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "image",
            source: {
              type: "base64",
              media_type: "image/png",
              data: cropped_img_base64,
            },
          },
          {
            type: "text",
            text: "Analyze the color season of the person in this image. Determine the single most likely season from these options: Light Spring, Warm Spring, Bright Spring, Light Summer, Cool Summer, Soft Summer, Soft Autumn, Warm Autumn, Deep Autumn, Deep Winter, Cool Winter, Bright Winter. Provide only the determined season name, with no additional explanation or commentary.",
          },
        ],
      },
    ],
  });

  for (const content of response.content) {
    if (content.type === "text") {
      return content.text;
    }
  }
  return "";
}

async function getAnalysis(cropped_img_base64: string, season: string) {
  const seasonEnum = season as Seasons;
  const seasonInfo = seasonsData[seasonEnum];

  if (!seasonInfo) {
    throw new Error(`Invalid season: ${season}`);
  }

  const getSeasonalColorsTool = {
    name: "get_seasonal_colors",
    description:
      "Get the suggested color palette and description based on the user's determined color season.",
    input_schema: {
      type: "object",
      properties: {
        season: {
          type: "string",
          enum: Object.values(Seasons),
          description: "The determined season of the user's skin tone.",
        },
      },
      required: ["season"],
    },
  };

  const messages = [
    {
      role: "user",
      content: [
        {
          type: "image",
          source: {
            type: "base64",
            media_type: "image/png",
            data: cropped_img_base64,
          },
        },
        {
          type: "text",
          text: `The person's color season is ${season}. Analyze the provided image for seasonal color typing using the provided seasonal colors information. Respond in JSON format with keys:"characteristics": Key features of person's coloring\n,"colorsToSuggest"(list): List of dicts with "name" and "hex_code" for 12 complementary colors\n"reasonToSuggest": Why these colors complement the person\n"colorsToAvoid"(list): List of dicts with "name" and "hex_code" for 12 unflattering colors (exclude uncommon clothing colors or extremely saturated hues)\n"reasonToAvoid": Why these colors clash with the person\n"content": <50 words explanation of season determination, starting with "Based on the image provided, you have..."`,
        },
      ],
    },
  ];

  const response = await anthropic.messages.create({
    model: "claude-3-5-sonnet-20240620",
    max_tokens: 1000,
    temperature: 0,
    system: SYSTEM_PROMPT,
    tools: [getSeasonalColorsTool],
    tool_choice: { type: "tool", name: "get_seasonal_colors" },
    messages,
  });

  messages.push({ role: "assistant", content: response.content });

  const toolUse = response.content[response.content.length - 1];
  if (toolUse.name === "get_seasonal_colors") {
    const toolResponse = {
      role: "user",
      content: [
        {
          type: "tool_result",
          tool_use_id: toolUse.id,
          content: JSON.stringify(seasonInfo),
        },
      ],
    };
    messages.push(toolResponse);
  }

  const followUpResponse = await anthropic.messages.create({
    model: "claude-3-5-sonnet-20240620",
    max_tokens: 1000,
    temperature: 0,
    system: SYSTEM_PROMPT,
    messages,
    tools: [getSeasonalColorsTool],
  });

  const message = followUpResponse.content[0].text;

  try {
    const jsonStart = message.indexOf("{");
    const jsonEnd = message.lastIndexOf("}");
    if (jsonStart === -1 || jsonEnd === -1) {
      throw new Error("No valid JSON object found in the response");
    }
    let jsonStr = message.slice(jsonStart, jsonEnd + 1);
    jsonStr = jsonStr.replace(/[\x00-\x1F\x7F-\x9F]/g, "");
    const extractedJson = JSON.parse(jsonStr);
    extractedJson.season = season;
    return extractedJson;
  } catch (error) {
    console.error("Error extracting JSON:", error);
    throw new Error("Failed to extract valid JSON from the response");
  }
}

export const POST: RequestHandler = async ({ request }) => {
  try {
    const body = await request.json();

    const { base64Image } = body;
    if (!base64Image) {
      return new Response(
        JSON.stringify({ error: "The image is not valid. Please try again." }),
        {
          status: 400,
          headers: {
            "Content-Type": "application/json",
          },
        },
      );
    }

    const season = await getSeason(base64Image);
    if (!season) {
      return new Response(
        JSON.stringify({
          error: "Failed to determine the season of the person in the image.",
        }),
        {
          status: 500,
          headers: {
            "Content-Type": "application/json",
          },
        },
      );
    }

    const analysis = await getAnalysis(base64Image, season);
    return new Response(JSON.stringify(analysis), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (error) {
    console.error("Error:", error);
    return new Response(
      JSON.stringify({
        error:
          "An error occurred when analyzing the image. Please try again later.",
      }),
      {
        status: 500,
        headers: {
          "Content-Type": "application/json",
        },
      },
    );
  }
};
