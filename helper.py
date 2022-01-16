import logging
import math

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by as by


def find_total_pages(amount, url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    elements_per_page = len(driver.find_elements(by=by.By.CLASS_NAME, value="js-post"))
    total_pages = math.ceil(amount / elements_per_page)

    logging.info(f"Total pages: {total_pages}")

    driver.close()

    return total_pages


def generate_urls(base_url, pages):
    urls = []
    for page in pages:
        if page == 0:
            urls.append(base_url)
            continue
        urls.append(f"{base_url}page/{page+1}")

    return urls
