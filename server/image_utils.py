import colorsys
import re
from enum import Enum
from typing import Any, Dict, List, Tuple

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


def get_analysis_by_skin_tone(skin_tone: str) -> Dict[str, Any]:
    """
    Analyze and provide color analysis based on skin tone.

    Args:
        skin_tone (str): A hex code representing the skin tone (without the '#').

    Returns:
        Dict[str, Any]: A dictionary containing the skin tone (with '#'),
                        the determined season, and the recommended colors.
    """
    season = get_season_by_skin_tone(skin_tone)
    colors = get_colors_by_skin_tone(skin_tone)
    skin_tone = "#" + skin_tone

    analysis = {"skin_tone": skin_tone, "season": season.value, "colors": colors}
    return analysis


def get_padded_facial_area(
    facial_area: List[int], width: int, height: int
) -> List[int]:
    """
    Calculate a padded bounding box around a given facial area.

    Args:
        facial_area (list): A list of four integers [x1, y1, x2, y2] representing
                            the top-left and bottom-right coordinates of the facial area of an image.
        width (int): The width of the image.
        height (int): The height of the image.

    Returns:
        list: A list of four integers [x1, y1, x2, y2] representing the top-left
              and bottom-right coordinates of the padded facial area.
    """
    center_x = (facial_area[0] + facial_area[2]) // 2
    center_y = (facial_area[1] + facial_area[3]) // 2

    padding = max(
        (facial_area[2] - center_x),
        (facial_area[3] - center_y),
    )

    padded_facial_area = [
        max(0, center_x - ((facial_area[2] - facial_area[0] + padding) // 2)),
        max(0, center_y - ((facial_area[3] - facial_area[1] + padding) // 2)),
        min(width, center_x + ((facial_area[2] - facial_area[0] + padding) // 2)),
        min(height, center_y + ((facial_area[3] - facial_area[1] + padding) // 2)),
    ]

    return padded_facial_area


def get_face(img_path: str) -> Tuple[List[Any], List[int]]:
    """
    Detect a face in the image and extract the facial area.

    Args:
        img_path (str): The path to the image file.

    Returns:
        Tuple[List[Any], List[int]]: A tuple containing the extracted face data and
                                     the facial area coordinates.

    Raises:
        MultipleFacesError: If more than one face is detected in the image.
        NoFacesError: If no face is detected in the image.
    """
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


def get_seasonal_palette(season: Season) -> List[str]:
    """
    Get a predefined color palette based on the given season.

    Args:
        season (Season): The season for which to retrieve the color palette.

    Returns:
        List[str]: A list of hex color codes representing the seasonal palette.
    """
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


def get_colors_by_skin_tone(skin_tone: str, num_colors: int = 12) -> List[str]:
    """
    Generate a palette of colors that complement the given skin tone.

    Args:
        skin_tone (str): The skin tone for which to generate the color palette.
        num_colors (int, optional): The number of colors to include in the palette. Defaults to 12.

    Returns:
        List[str]: A list of hex color codes that complement the given skin tone.
    """
    season = get_season_by_skin_tone(skin_tone)
    palette = get_seasonal_palette(season)

    # If num_colors is less than the full palette, select a subset
    if num_colors < len(palette):
        step = len(palette) // num_colors
        return [palette[i] for i in range(0, len(palette), step)][:num_colors]

    return palette[:num_colors]


def get_season_by_skin_tone(skin_tone: str) -> Season:
    """
    Determine the season based on the given skin tone.

    Args:
        skin_tone (str): A hex code representing the skin tone.

    Returns:
        Season: The season corresponding to the skin tone.
    """
    rgb_color = hex_to_rgb(skin_tone)
    r, g, b = rgb_color[0] / 255, rgb_color[1] / 255, rgb_color[2] / 255
    h, lightness, s = colorsys.rgb_to_hls(r, g, b)

    # Determine undertone (hue)
    if 0.5 < h <= 0.75:  # More blue/purple hues
        undertone = "cool"
    elif 0 <= h <= 0.25 or 0.75 < h <= 1:  # More red/yellow hues
        undertone = "warm"
    else:  # Green hues or neutral
        undertone = "neutral"

    # Determine value (light vs dark)
    value = "light" if lightness > 0.5 else "dark"

    # Determine chroma (muted vs bright)
    chroma = "bright" if s > 0.5 else "muted"

    # Map to seasons
    if undertone == "cool":
        return Season.WINTER if value == "dark" or chroma == "bright" else Season.SUMMER
    else:  # warm or neutral
        return Season.AUTUMN if value == "dark" or chroma == "muted" else Season.SPRING


def is_hex_color(hex_color: str) -> bool:
    """
    Validate if the input string is a valid hexadecimal color code.

    Args:
        hex_color (str): The hex color code to validate. The "#" is optional.

    Returns:
        bool: True if valid hex color code, False otherwise.
    """
    return bool(re.match(r"^#?(?:[0-9a-fA-F]{3}){1,2}$", hex_color))


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Convert hex color to RGB tuple.

    Args:
        hex_color (str): The hex color code to convert.

    Returns:
        Tuple[int, int, int]: The RGB representation of the hex color.
    """
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError("Invalid hex color format")

    r, g, b = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    return (r, g, b)


def rgb_to_hex(rgb_color: Tuple[int, int, int]) -> str:
    """
    Convert RGB tuple to hex color.

    Args:
        rgb_color (Tuple[int, int, int]): The RGB color to convert.

    Returns:
        str: The hex representation of the RGB color.
    """
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)
