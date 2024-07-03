import random
import string
from PIL import Image, ImageDraw, ImageFont


def generate_captcha(length=6):
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    image = Image.new('RGB', (200, 80), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    font = ImageFont.truetype('arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    draw.text((20, 20), captcha_text, font=font, fill=(0, 0, 0))
    image_path = "captcha.png"
    image.save(image_path)
    return captcha_text, image_path


def validate_captcha(user_input, captcha_text):
    return user_input == captcha_text
