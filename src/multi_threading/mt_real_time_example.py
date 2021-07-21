import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097'
]


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


def download_in_sync_manner():
    start_time = time.perf_counter()
    for img_url in img_urls:
        download_image(img_url)
    end_time = time.perf_counter()
    print(f'Finished in {round(end_time-start_time, 2)} second(s)')

def download_using_threads():
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)
    end_time = time.perf_counter()
    print(f'Finished in {round(end_time-start_time, 2)} second(s)')


if __name__ == "__main__":
    # download_in_sync_manner()

    download_using_threads()
