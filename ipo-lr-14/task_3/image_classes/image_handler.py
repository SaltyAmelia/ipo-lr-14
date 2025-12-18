from PIL import Image

class ImageHandler:
    def __init__(self, path):
        self.path = path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.path)
        print("Изображение успешно загружено")

    def make_thumbnail(self):
        self.image.thumbnail((200, 200))
        print("Размер изображения изменен на 200x200")

    def save_with_new_name(self, filename):
        self.image.save(filename)
        print(f"Изображение сохранено как {filename}")

    def get_image(self):
        return self.image   
