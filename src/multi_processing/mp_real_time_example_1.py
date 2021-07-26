import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg'
]


size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


def process_image_with_multi_process():
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)
    print(f'Finished in {round(t2-t1, 2)} seconds')


if __name__ == "__main__":
    process_image_with_multi_process()
