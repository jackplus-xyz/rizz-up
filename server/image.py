import logging
import io
import base64
import tempfile

import stone
from flask import Blueprint, jsonify, request
from PIL import Image

from image_utils import (
    MultipleFacesError,
    NoFacesError,
    get_face,
    get_padded_facial_area,
)

bp = Blueprint("image_api", __name__, url_prefix="/image")


@bp.route("/", methods=["POST"])
def get_skin_tone_and_facial_area_from_image():
    file = request.files.get("image")
    if not file or file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        with tempfile.NamedTemporaryFile(
            suffix=".png"
        ) as temp_file, tempfile.NamedTemporaryFile(suffix=".png") as face_file:
            file.save(temp_file.name)
            original_img = Image.open(temp_file.name)
            width, height = original_img.size

            face_img, facial_area = get_face(temp_file.name)
            face_img = Image.fromarray(face_img[0])
            face_img.save(face_file.name)

            result = stone.process(
                face_file.name, image_type="color", return_report_image=True
            )

        skin_tone = result["faces"][0].get("skin_tone").lower()

        facial_area = [int(area) for area in facial_area]

        padded_facial_area = get_padded_facial_area(
            facial_area,
            width,
            height,
        )

        x1, y1, x2, y2 = padded_facial_area
        cropped_img = original_img.crop((x1, y1, x2, y2))

        cropped_img_bytes = io.BytesIO()
        cropped_img.save(cropped_img_bytes, format="PNG")
        cropped_img_bytes.seek(0)
        cropped_img_base64 = base64.b64encode(cropped_img_bytes.read()).decode("utf-8")

        return jsonify(
            {
                "skin_tone": skin_tone,
                "cropped_image": cropped_img_base64,
            }
        )

    except NoFacesError:
        return jsonify(
            {
                "error": "No face detected in the image. Please upload an image with a clearly visible face in natural lighting."
            }
        ), 400
    except MultipleFacesError:
        return jsonify(
            {
                "error": "Multiple faces detected in the image. Please upload an image with only one face."
            }
        ), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({"error": "Unexpected error occurred."}), 500
