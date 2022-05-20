import schedule
import time
from copy import copy
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw
from tinyWinToast.tinyWinToast import Toast
from text import TEXT


def notify(image) -> None:
    toast = Toast()
    toast.setTitle("hi", maxLines=1)
    toast.setImage(str(image))
    toast.show()
    # Path(image).unlink()


def add_text(
        image: Image,
        xy: tuple,
        text: str,
        font: ImageFont,
        stroke_width: int,
        stroke_fill: tuple,
        spacing=0,
        fill=(0, 0, 0)
) -> Image:
    draw = ImageDraw.Draw(image, "RGB")
    draw.text(xy=xy,
              text=text,
              spacing=spacing,
              font=font,
              fill=fill,
              stroke_width=stroke_width,
              stroke_fill=stroke_fill)
    return image


def image_editor(image_path: Path, font_path: Path, text: tuple) -> Path:
    with Image.open(image_path) as image:
        width, height = image.size
        font = ImageFont.truetype(font=str(font_path), size=24)

        for val in text:
            new_image = copy(image)
            new_image = add_text(xy=(width // 2 - font.getsize(val[0])[0] // 2, 10),
                                 image=new_image,
                                 text=val[0],
                                 font=font,
                                 fill=(255, 255, 255),
                                 stroke_width=2,
                                 stroke_fill=(0, 0, 0))
            new_image = add_text(xy=(width // 2 - font.getsize(val[1])[0] // 2, height - 30),
                                 image=new_image,
                                 text=val[1],
                                 font=font,
                                 fill=(255, 255, 255),
                                 stroke_width=2,
                                 stroke_fill=(0, 0, 0))

        new_image.save(Path(Path(image_path).parent, 'temp.jpg'))
        return Path(Path(image_path).parent, 'temp.jpg')


if __name__ == "__main__":
    image_path = str(Path(Path.cwd(), 'static', 'img', 'blank.jpg'))
    font_path = str(Path(Path.cwd(), 'static', 'fonts', 'Roboto-Bold.ttf'))

    schedule.every().day.at('14:58:00').do(notify, image=image_editor(image_path, font_path, [["Не пропусти", "уведомления"]]))
    schedule.every().day.at('14:58:17').do(notify, image=image_editor(image_path, font_path, [["Доброе утро", "Иван"]]))


    while True:
        schedule.run_pending()
        time.sleep(1)
