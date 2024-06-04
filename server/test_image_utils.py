import pytest
from image_utils import is_hex_color


# Parametrized tests for the 'is_hex_color' function
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
