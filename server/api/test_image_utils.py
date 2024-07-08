import pytest
import os
import random
from image_utils import get_face, is_hex_color
from PIL import Image, ImageDraw

img_files = os.listdir("test_images")


def test_get_padded_facial_area():
    img_path = random.choice(img_files)
    facial_area = get_face(img_path)

    # Open image with PIL
    image_pil = Image.open(img_path)
    draw = ImageDraw.Draw(image_pil)
    for point in facial_area:
        draw.point(point, fill=(0, 255, 0))

    image_pil.show()


@pytest.mark.parametrize(
    "hex_color, expected",
    [
        ("#FFFFFF", True),
        ("#000000", True),
        ("#ff0000", True),
        ("#0f0", True),
        ("#00FF00", True),
        ("#abc", True),
        ("#123456", True),
        ("FFFFFF", False),
        ("#FFFFF", False),
        ("#GGGGGG", False),
        ("#12345G", False),
        ("#1234567", False),
        ("#12", False),
        ("#XYZ123", False),
        ("#12345z", False),
        ("#1", False),
        ("#", False),
        ("", False),
    ],
)
def test_is_hex_color(hex_color, expected):
    assert (
        is_hex_color(hex_color) == expected
    ), f"Hex color {hex_color} validation failed."
