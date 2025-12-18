from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        print("Применён фильтр контуров")

    def add_text_center(self, text):
        draw = ImageDraw.Draw(self.image)
        width, height = self.image.size

        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (width - text_width) // 2
        y = (height - text_height) // 2

        draw.text((x, y), text, fill="black", font=font)
        print("Текст добавлен в центр изображения")

    def get_image(self):
        return self.image
