from flask import Blueprint, abort, jsonify

from image_utils import (
    get_analysis_by_skin_tone,
    is_hex_color,
)

bp = Blueprint("palette_api", __name__, url_prefix="/palette")


@bp.route("/hex/<hex_skin_tone>", methods=["GET"])
def get_hex_analysis(hex_skin_tone):
    if is_hex_color(hex_skin_tone):
        analysis = get_analysis_by_skin_tone(hex_skin_tone)
        return jsonify(analysis), 200

    abort(400, "Invalid hexadecimal color code")
