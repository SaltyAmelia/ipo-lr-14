from image_classes.image_handler import ImageHandler
from image_classes.image_processor import ImageProcessor

def main():
    path = input("Введите путь к изображению: ").strip()
    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1]

    handler = ImageHandler(path)
    handler.load_image()
    handler.make_thumbnail()

    image = handler.get_image()
    processor = ImageProcessor(handler.image)

    processor.apply_contour()
    processor.add_text_center("Вариант 3")

    handler.image = processor.get_image()
    handler.save_with_new_name("result_variant3.jpg")

if __name__ == "__main__":
    main()
