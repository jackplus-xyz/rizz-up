import { dev } from "$app/environment";
import {
  GOOGLE_CLOUD_RUN_URL,
  GOOGLE_CLOUD_PROJECT_ID,
  GOOGLE_CLOUD_CLIENT_EMAIL,
  GOOGLE_CLOUD_PRIVATE_KEY,
} from "$env/static/private";
import type { RequestHandler } from "@sveltejs/kit";
import { GoogleAuth } from "google-auth-library";

async function getAuthenticatedClient() {
  const auth = new GoogleAuth({
    credentials: {
      private_key: GOOGLE_CLOUD_PRIVATE_KEY.replace(/\\n/g, "\n"),
      client_email: GOOGLE_CLOUD_CLIENT_EMAIL,
      project_id: GOOGLE_CLOUD_PROJECT_ID,
    },
    scopes: "https://www.googleapis.com/auth/cloud-platform",
  });
  return auth.getClient();
}

export const POST: RequestHandler = async ({ request }) => {
  try {
    const formData = await request.formData();
    const client = await getAuthenticatedClient();
    const authHeaders = await client.getRequestHeaders();
    const apiUrl = dev
      ? "http://localhost:8080/api/images/crop"
      : `${GOOGLE_CLOUD_RUN_URL}/api/images/crop`;

    const headers = new Headers(authHeaders);
    // Remove the Content-Type header if it exists
    // This allows the browser to set the correct Content-Type with boundary for FormData
    headers.delete("Content-Type");

    const response = await fetch(apiUrl, {
      method: "POST",
      headers: headers,
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
