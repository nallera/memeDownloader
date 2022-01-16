import threading
from concurrent import futures
import logging
import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by as by

from helper import find_total_pages, generate_urls


def download_memes(base_url, local_folder, amount, workers):
    start_time = time.time()

    total_pages = find_total_pages(amount, base_url)

    image_urls = extract_image_urls(base_url, amount, workers, total_pages)

    download_images_from_urls(image_urls, local_folder, workers)

    end_time = time.time()

    logging.info(f"{len(image_urls)} meme images were downloaded successfully to {local_folder}")
    logging.info(f"The program took {end_time - start_time:.2f} seconds to run")


def download_images_from_urls(image_urls, local_folder, workers):
    logging.info("Downloading images")

    image_urls = [(index, image_url) for index, image_url in enumerate(image_urls)]

    arguments = [(image_url, local_folder) for image_url in image_urls]

    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(lambda p: download_image_from_url(*p), arguments)


def download_image_from_url(image_url, local_folder):
    image_index = image_url[0]
    actual_image_url = image_url[1]

    image_req = requests.get(actual_image_url)
    image_file = open(f"{local_folder}\\{image_index + 1}.jpg", 'wb')
    image_file.write(image_req.content)
    image_file.close()


def extract_image_urls(base_url, amount, workers, total_pages):
    image_urls = []

    worker_assignment = [list(range(j, total_pages, workers)) for j in range(workers)]
    lock = threading.Lock()

    arguments = [(base_url, pages, image_urls, lock) for pages in worker_assignment]

    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(lambda p: crawl_memes(*p), arguments)

    image_urls.sort()
    image_urls = [image_url for page, index, image_url in image_urls]

    return image_urls[:amount]


def crawl_memes(base_url, pages, image_urls, lock):
    threading.current_thread().name = f"thread{pages[0]}"

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    urls = generate_urls(base_url, pages)

    for url in urls:
        driver.get(url)

        page_number = "1" if "page" not in url else url.split("/")[-1]

        logging.info(f"Crawling page {page_number}")
        meme_elements = driver.find_elements(by=by.By.CLASS_NAME, value="js-post")

        if len(meme_elements) == 0:
            logging.info("No sections containing memes were found")
            break

        for index, element in enumerate(meme_elements):
            image_element = element.find_element(by.By.TAG_NAME, "img")
            lock.acquire()
            image_urls.append((page_number, index, image_element.get_attribute("data-src")))
            lock.release()

    driver.close()
