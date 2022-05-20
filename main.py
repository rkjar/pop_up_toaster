import schedule
import time
from copy import copy
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw
from tinyWinToast.tinyWinToast import Toast
from text import TEXT


def notify(image: Path, text: tuple[str]) -> None:
    toast = Toast()
    # toast.setTitle(" ".join([word for word in text]), maxLines=1)
    toast.setImage(str(image))
    toast.setAppID(" ".join([word for word in text]))
    toast.show()


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
        text_double_list = []
        text_double_list.append(text)

        for val in text_double_list:
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


def main(image_path: Path, font_path: Path):
    value = time.strftime("%H:%M")
    if value == "08:00":
        notify(image_editor(image_path, font_path, TEXT[0]), TEXT[0])

    elif value == "08:03":
        notify(image_editor(image_path, font_path, TEXT[1]), TEXT[1])

    elif value == "09:30":
        notify(image_editor(image_path, font_path, TEXT[4]), TEXT[4])

    elif value == "10:29":
        notify(image_editor(image_path, font_path, TEXT[3]), TEXT[3])

    elif value == "12:30":
        notify(image_editor(image_path, font_path, TEXT[4]), TEXT[4])

    elif value == "17:00":
        notify(image_editor(image_path, font_path, TEXT[4]), TEXT[4])

    elif value == "18:30":
        notify(image_editor(image_path, font_path, TEXT[6]), TEXT[6])

    elif value == "19:55":
        notify(image_editor(image_path, font_path, TEXT[5]), TEXT[5])

    elif value == "20:03":
        notify(image_editor(image_path, font_path, TEXT[7]), TEXT[7])


if __name__ == "__main__":
    image_path = str(Path(Path.cwd(), 'static', 'img', 'blank.jpg'))
    font_path = str(Path(Path.cwd(), 'static', 'fonts', 'Roboto-Bold.ttf'))
    schedule.every().minutes.do(main, image_path=image_path, font_path=font_path)

    while True:
        schedule.run_pending()
        time.sleep(1)