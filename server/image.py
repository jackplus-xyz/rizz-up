import logging
import tempfile

import stone
from flask import Blueprint, jsonify, request
from PIL import Image

from image_utils import (
    MultipleFacesError,
    NoFacesError,
    get_face,
)

bp = Blueprint("image_api", __name__, url_prefix="/image")


@bp.route("/", methods=["POST"])
def get_skin_tone_from_image():
    file = request.files.get("image")
    if not file or file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        with tempfile.NamedTemporaryFile(suffix=".png") as temp_file:
            file.save(temp_file.name)
            face_img, facial_area = get_face(temp_file.name)

            img = Image.fromarray(face_img[0])
            img.save(temp_file.name)

            result = stone.process(
                temp_file.name, image_type="color", return_report_image=True
            )
            skin_tone = result["faces"][0].get("skin_tone").lower()
            facial_area = [int(area) for area in facial_area]

            return jsonify({"skin_tone": skin_tone, "facial_area": facial_area})

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
