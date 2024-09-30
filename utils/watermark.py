from PIL import Image, ImageDraw, ImageFont

def apply_text_watermark(image, text, font_path="arial.ttf", font_size=36):
    """
    Apply a text watermark to the given image.

    :param image: The image to which the watermark will be applied (PIL Image object).
    :param text: The text to use as a watermark.
    :param font_path: The path to the font file (default: arial.ttf).
    :param font_size: The size of the font (default: 36).
    :return: The watermarked image (PIL Image object).
    """
    draw = ImageDraw.Draw(image)
    font = _load_font(font_path, font_size)
    x, y = _calculate_watermark_position(image, text, font)
    
    # Change the fill color to a semi-transparent black for better visibility
    draw.text((x, y), text, font=font, fill=(0, 0, 0, 128))  # Semi-transparent black text
    return image

def _load_font(font_path, font_size):
    """
    Load the font from the given path, or use the default font if loading fails.

    :param font_path: The path to the font file.
    :param font_size: The size of the font.
    :return: The loaded font.
    """
    try:
        return ImageFont.truetype(font_path, font_size)
    except IOError:
        return ImageFont.load_default()

def _calculate_watermark_position(image, text, font):
    """
    Calculate the position for the watermark text.

    :param image: The image to which the watermark will be applied (PIL Image object).
    :param text: The text to use as a watermark.
    :param font: The font used for the watermark text.
    :return: A tuple (x, y) representing the position for the watermark.
    """
    draw = ImageDraw.Draw(image)
    bbox = draw.textbbox((0, 0), text, font=font)
    textwidth, textheight = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = image.width - textwidth - 10
    y = image.height - textheight - 10
    return x, y