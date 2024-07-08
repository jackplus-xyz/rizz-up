import os
import re
from typing import Any, List, Tuple

from dotenv import load_dotenv
from retinaface import RetinaFace

load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


class MultipleFacesError(Exception):
    """Custom exception for multiple faces detected."""

    pass


class NoFacesError(Exception):
    """Custom exception for multiple faces detected."""

    pass


def get_padded_facial_area(
    facial_area: List[int], width: int, height: int
) -> Tuple[int, int, int, int]:
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

    return (
        max(0, center_x - ((facial_area[2] - facial_area[0] + padding) // 2)),
        max(0, center_y - ((facial_area[3] - facial_area[1] + padding) // 2)),
        min(width, center_x + ((facial_area[2] - facial_area[0] + padding) // 2)),
        min(height, center_y + ((facial_area[3] - facial_area[1] + padding) // 2)),
    )


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
