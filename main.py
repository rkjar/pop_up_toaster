from copy import copy

import schedule
import time
from pathlib import Path
from tinyWinToast.tinyWinToast import Toast
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


def notify():
    toast = Toast()
    toast.setTitle("hi", maxLines=1)
    toast.setImage(str(Path(Path.cwd(), 'hi.png')))
    toast.show()


def add_text(image: Image, xy: tuple, text: str, spacing=0, fill=(0, 0, 0)) -> Image:
    draw = ImageDraw.Draw(image, "RGB")
    draw.text(xy=xy,
              text=text,
              spacing=spacing,
              fill=fill)
    return image


def image_editor(blank_image: Path, text: tuple):
    with Image.open(blank_image) as image:
        width, height = image.size
        for key, val in text.items():
            new_image = copy(image)
            new_image = add_text(image=new_image,
                             xy=(width // 2, 30),
                             text=key,
                             fill=(255, 255, 255))
            new_image = add_text(image=new_image,
                             xy=(width // 2, height - 70),
                             text=val,
                             fill=(255, 255, 255))
            new_image.show()


# schedule.every(1).minutes.do(notify)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
text = {'Darova' : 'Vanya', 'Dobroe utro' : 'Vanya', 'Ivan' : 'KEK'}
image_path = str(Path(Path.cwd(), 'blank.jpg'))
image_editor(image_path, text)