from random import choice
from string import ascii_uppercase, digits
from PIL import Image

from captcha.image import ImageCaptcha


def create_captcha():
    captcha_text = text_generator()
    image = generate_image_captcha(captcha_text)
    return image, captcha_text


def generate_image_captcha(text_captcha):
    image = ImageCaptcha(width=280, height=90)
    image.generate(text_captcha)
    image.write(text_captcha, "out.png")
    return Image.open("out.png")


def text_generator(size=6, chars=ascii_uppercase + digits):
    return "".join(choice(chars) for _ in range(size))
