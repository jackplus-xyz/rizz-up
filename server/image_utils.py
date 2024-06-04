import colorsys
import re
from enum import Enum

from retinaface import RetinaFace


class MultipleFacesError(Exception):
    """Custom exception for multiple faces detected."""

    pass


class NoFacesError(Exception):
    """Custom exception for multiple faces detected."""

    pass


class Season(Enum):
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"


def get_analysis_by_skin_tone(skin_tone):
    season = get_season_by_skin_tone(skin_tone)
    colors = get_colors_by_skin_tone(skin_tone)
    # TODO:Add not recommended colors

    return {"skinTone": "#" + skin_tone, "season": season.value, "colors": colors}


def get_face(img_path):
    """Detect the faces in the image."""
    faces = RetinaFace.detect_faces(img_path=img_path)

    if faces:
        if len(faces) > 1:
            raise MultipleFacesError(
                "Found multiple faces. Please upload an image that only contains one face."
            )

        for key in faces.keys():
            identity = faces[key]
            if identity["score"] > 0.9:
                face = RetinaFace.extract_faces(img_path=img_path, align=True)
                facial_area = identity["facial_area"]
                return (face, facial_area)

    raise NoFacesError(
        "No face detected in the image. Please upload an image with a clearly visible face in natural lighting."
    )


def get_seasonal_palette(season):
    palettes = {
        Season.WINTER: [
            "#0000FF",
            "#FF00FF",
            "#FFFFFF",
            "#000000",
            "#800080",
            "#0080FF",
            "#FF0080",
            "#404040",
            "#8080FF",
            "#FF8080",
            "#008080",
            "#800000",
        ],
        Season.SUMMER: [
            "#87CEEB",
            "#DDA0DD",
            "#E6E6FA",
            "#B0C4DE",
            "#778899",
            "#AFEEEE",
            "#FFC0CB",
            "#F0F8FF",
            "#E0FFFF",
            "#FFE4E1",
            "#F5F5F5",
            "#F5FFFA",
        ],
        Season.AUTUMN: [
            "#8B4513",
            "#A0522D",
            "#D2691E",
            "#CD853F",
            "#DEB887",
            "#DAA520",
            "#B8860B",
            "#800020",
            "#8B0000",
            "#A52A2A",
            "#D2B48C",
            "#F4A460",
        ],
        Season.SPRING: [
            "#FFD700",
            "#FFA500",
            "#FF6347",
            "#FF69B4",
            "#FFB6C1",
            "#FFC0CB",
            "#7FFF00",
            "#00FF7F",
            "#98FB98",
            "#ADFF2F",
            "#F0E68C",
            "#FAFAD2",
        ],
    }
    return palettes[season]


def get_colors_by_skin_tone(skin_tone, num_colors=12):
    """Generate a palette of colors that complement the given hex color."""
    season = get_season_by_skin_tone(skin_tone)
    palette = get_seasonal_palette(season)

    # If num_colors is less than the full palette, select a subset
    if num_colors < len(palette):
        step = len(palette) // num_colors
        return [palette[i] for i in range(0, len(palette), step)][:num_colors]

    return palette[:num_colors]


def get_season_by_skin_tone(skin_tone):
    rgb_color = hex_to_rgb(skin_tone)
    r, g, b = rgb_color[0] / 255, rgb_color[1] / 255, rgb_color[2] / 255
    h, l, s = colorsys.rgb_to_hls(r, g, b)

    # Determine undertone (hue)
    if 0.5 < h <= 0.75:  # More blue/purple hues
        undertone = "cool"
    elif 0 <= h <= 0.25 or 0.75 < h <= 1:  # More red/yellow hues
        undertone = "warm"
    else:  # Green hues or neutral
        undertone = "neutral"

    # Determine value (light vs dark)
    value = "light" if l > 0.5 else "dark"

    # Determine chroma (muted vs bright)
    chroma = "bright" if s > 0.5 else "muted"

    # Map to seasons
    if undertone == "cool":
        return Season.WINTER if value == "dark" or chroma == "bright" else Season.SUMMER
    else:  # warm or neutral
        return Season.AUTUMN if value == "dark" or chroma == "muted" else Season.SPRING


def is_hex_color(hex_color):
    """Validate if the input string is a valid hexadecimal color code."""
    return re.match(r"^#?(?:[0-9a-fA-F]{3}){1,2}$", hex_color)


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    """Convert RGB tuple to hex color."""
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)
