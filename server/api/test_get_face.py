import os
import random

from PIL import Image, ImageDraw

from image_utils import get_face, get_padded_facial_area

DATA_DIR = os.path.expanduser("~/Developer/data/ffhq-dataset/00000/")
img_files = [f for f in os.listdir(DATA_DIR) if f.endswith((".jpg", ".png"))]


def test_get_padded_facial_area():
    img_path = os.path.join(DATA_DIR, random.choice(img_files))
    original_image = Image.open(img_path)
    original_width, original_height = original_image.size

    original_image_copy = original_image.copy()
    _, facial_area = get_face(img_path)
    padded_facial_area = get_padded_facial_area(
        facial_area,
        original_width,
        original_height,
    )
    facial_area = tuple(facial_area)
    padded_facial_area = tuple(padded_facial_area)

    cropped_image = original_image_copy.crop(facial_area)
    padded_cropped_image = original_image_copy.crop(padded_facial_area)

    draw = ImageDraw.Draw(original_image_copy)
    for point in facial_area:
        draw.point(point, fill=(0, 255, 0))

    # Create a new image to display all three images side by side
    combined_image = Image.new("RGB", (original_width * 3, original_height))
    combined_image.paste(original_image_copy, (0, 0))
    combined_image.paste(cropped_image, (original_width, 0))
    combined_image.paste(padded_cropped_image, (original_width * 2, 0))

    combined_image.show()
    combined_image.close()


test_get_padded_facial_area()
