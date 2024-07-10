import { GOOGLE_CLOUD_RUN_URL } from "$env/static/private";

/** @param {FormData} formData */
async function getCroppedImage(formData) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 60000);

  try {
    const response = await fetch(`${GOOGLE_CLOUD_RUN_URL}/api/images/crop`, {
      method: "POST",
      body: formData,
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      console.error(response);
      throw new Error("Failed to process image");
    }

    const responseData = await response.json();

    if (responseData.error) {
      throw new Error(responseData.error);
    }

    return responseData.cropped_image;
  } catch (error) {
    clearTimeout(timeoutId);
    throw error;
  }
}

/** @type {import('./$types').RequestHandler} */
export const POST = async ({ request }) => {
  try {
    const formData = await request.formData();
    const croppedImage = await getCroppedImage(formData);

    return new Response(JSON.stringify({ croppedImage }), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (error) {
    console.error("Error processing image:", error);
    if (error instanceof Error) {
      if (error.name === "AbortError") {
        return new Response("Request timed out", { status: 408 });
      }
      if (error.message === "Failed to process image") {
        return new Response(error.message, { status: 500 });
      }
      return new Response(error.message, { status: 400 });
    }
    return new Response("An unknown error occurred", { status: 500 });
  }
};
