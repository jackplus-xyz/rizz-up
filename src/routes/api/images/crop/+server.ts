import { dev } from "$app/environment";
import { SERVER_URL } from "$env/static/private";
import type { RequestHandler } from "@sveltejs/kit";

export const POST: RequestHandler = async ({ request }) => {
  try {
    const formData = await request.formData();

    const apiUrl = dev
      ? "http://localhost:8080/api/images/crop"
      : `${SERVER_URL}/api/images/crop`;

    const response = await fetch(apiUrl, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
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
