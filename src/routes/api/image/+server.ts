import type { RequestHandler } from "@sveltejs/kit";
import * as tf from "@tensorflow/tfjs";
import * as blazeface from "@tensorflow-models/blazeface";
import "@tensorflow/tfjs-backend-wasm";
import sharp from "sharp";

let model: blazeface.BlazeFaceModel | null = null;

export const POST: RequestHandler = async ({ request }) => {
  try {
    if (!model) {
      await tf.ready();
      model = await blazeface.load();
    }

    const formData = await request.formData();
    const imageFile = formData.get("image") as File;
    if (!imageFile) {
      return new Response("No image provided", { status: 400 });
    }

    const imageData = await imageFile.arrayBuffer();
    const imageBuffer = Buffer.from(imageData);

    // Use sharp to process the image
    const image = sharp(imageBuffer);
    const { data, info } = await image
      .raw()
      .toBuffer({ resolveWithObject: true });

    const tensor = tf.tensor3d(new Uint8Array(data), [
      info.height,
      info.width,
      info.channels,
    ]);

    const predictions = await model.estimateFaces(tensor, false);

    if (predictions.length < 1) {
      return new Response(
        JSON.stringify({
          error: "No faces found in the image, please try with another image",
        }),
        {
          status: 400,
          headers: { "Content-Type": "application/json" },
        },
      );
    }
    if (predictions.length > 1) {
      return new Response(
        JSON.stringify({
          error:
            "More than one face found in the image, please upload an image with only one face",
        }),
        {
          status: 400,
          headers: { "Content-Type": "application/json" },
        },
      );
    }

    const [topLeft, bottomRight] = [
      predictions[0].topLeft,
      predictions[0].bottomRight,
    ];
    const [x, y] = topLeft as [number, number];
    const [x2, y2] = bottomRight as [number, number];

    // Calculate the center of the face
    const centerX = (x + x2) / 2;
    const centerY = (y + y2) / 2;

    // Calculate the dimensions of the face
    const faceWidth = x2 - x;
    const faceHeight = y2 - y;

    // Extend the crop area
    const extensionFactor = 2;
    let extendedWidth = faceWidth * extensionFactor;
    let extendedHeight = faceHeight * extensionFactor;

    // Calculate new crop boundaries
    let left = Math.round(centerX - extendedWidth / 2);
    let top = Math.round(centerY - extendedHeight / 2);
    let width = Math.round(extendedWidth);
    let height = Math.round(extendedHeight);

    // Ensure crop doesn't exceed image boundaries
    left = Math.max(0, left);
    top = Math.max(0, top);
    width = Math.min(width, info.width - left);
    height = Math.min(height, info.height - top);

    const croppedImage = await image
      .extract({ left, top, width, height })
      .resize(224, 224)
      .png()
      .toBuffer();

    // Return the processed image in the response
    return new Response(croppedImage, {
      headers: {
        "Content-Type": "image/png",
        "Content-Length": croppedImage.length.toString(),
      },
    });
  } catch (error) {
    console.error("Error processing image:", error);
    return new Response("Internal Server Error", { status: 500 });
  }
};
