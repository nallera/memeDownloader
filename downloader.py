import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by as by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_memes(url, local_folder, amount):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    image_urls = extract_image_urls(driver, amount)

    driver.close()

    for index, image_url in enumerate(image_urls):
        download_image_from_url(image_url, index, local_folder)

    print(f"{len(image_urls)} meme images were downloaded successfully to {local_folder}")


def download_image_from_url(image_url, index, local_folder):
    image_req = requests.get(image_url)
    image_file = open(f"{local_folder}\\{index + 1}.jpg", 'wb')
    image_file.write(image_req.content)
    image_file.close()


def extract_image_urls(driver, amount):
    meme_elements = []
    image_urls = []

    while len(image_urls) < amount:
        meme_elements = driver.find_elements(by=by.By.CLASS_NAME, value="js-post")

        if len(meme_elements) == 0:
            print("No sections containing memes were found")
            break

        for index, element in enumerate(meme_elements):
            image_element = element.find_element(by.By.TAG_NAME, "img")
            image_urls.append(image_element.get_attribute("data-src"))

        if len(image_urls) < amount:
            pager = driver.find_element(by.By.CLASS_NAME, "mu-pager")
            next_button = pager.find_elements(by.By.TAG_NAME, "a")[-1]
            next_button.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((by.By.CLASS_NAME, "js-post"))
            )

    return image_urls[:amount]
