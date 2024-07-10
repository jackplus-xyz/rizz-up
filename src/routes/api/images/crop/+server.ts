import { GOOGLE_CLOUD_RUN_URL } from "$env/static/private";
import type { RequestHandler } from "@sveltejs/kit";

export const maxDuration = 60; // This function can run for a maximum of 60 seconds

export const POST: RequestHandler = async ({ request }) => {
  try {
    const formData = await request.formData();

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 60000);

    const response = await fetch(`${GOOGLE_CLOUD_RUN_URL}/api/images/crop`, {
      method: "POST",
      body: formData,
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      console.error(response);
      return new Response("Failed to process image", {
        status: response.status,
      });
    }

    const responseData = await response.json();

    if (responseData.error) {
      return new Response(responseData.error, { status: 400 });
    }

    return new Response(
      JSON.stringify({ croppedImage: responseData.cropped_image }),
      {
        status: 200,
        headers: {
          "Content-Type": "application/json",
        },
      },
    );
  } catch (error) {
    console.error("Error processing image:", error);
    if (error instanceof Error) {
      if (error.name === "AbortError") {
        return new Response("Request timed out", { status: 408 });
      }
      return new Response(`Error: ${error.message}`, { status: 500 });
    }
    return new Response("An unknown error occurred", { status: 500 });
  }
};
