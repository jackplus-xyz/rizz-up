import { GOOGLE_CLOUD_RUN_URL } from "$env/static/private";
import type { RequestHandler } from "@sveltejs/kit";

export const POST: RequestHandler = async ({ request }) => {
  try {
    const formData = await request.formData();

    const response = await fetch(`${GOOGLE_CLOUD_RUN_URL}/api/images/crop`, {
      method: "POST",
      body: formData,
    });

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

    // Return the cropped image data
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
    return new Response("Internal Server Error", { status: 500 });
  }
};
