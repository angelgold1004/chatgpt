import os
from pathlib import Path
from urllib.parse import quote

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def scrape(keyword: str, image_dir: str = "naver_news_images"):
    """Scrape Naver news search results for the given keyword.

    Parameters
    ----------
    keyword: str
        Search keyword for Naver news.
    image_dir: str
        Directory where thumbnail images will be stored.
    """
    url = f"https://search.naver.com/search.naver?where=news&query={quote(keyword)}"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    titles = []
    links = []
    image_srcs = []

    news_items = driver.find_elements(By.CSS_SELECTOR, "div.news_wrap.api_ani_send")
    for item in news_items:
        title_el = item.find_element(By.CSS_SELECTOR, "a.news_tit")
        titles.append(title_el.text)
        links.append(title_el.get_attribute("href"))

        try:
            img_el = item.find_element(By.CSS_SELECTOR, "img.thumb")
            src = img_el.get_attribute("src")
            if src:
                image_srcs.append(src)
        except Exception:
            pass

    driver.quit()

    # Save images
    img_dir = Path(image_dir)
    img_dir.mkdir(parents=True, exist_ok=True)
    for idx, src in enumerate(image_srcs, 1):
        try:
            response = requests.get(src, timeout=10)
            response.raise_for_status()
            extension = src.split("?")[0].split(".")[-1]
            (img_dir / f"image_{idx}.{extension}").write_bytes(response.content)
        except Exception:
            continue

    return titles, links, image_srcs


if __name__ == "__main__":
    keyword = input("네이버에서 검색할 키워드를 입력하세요: ")
    titles, links, images = scrape(keyword)

    for t, l in zip(titles, links):
        print(f"{t} - {l}")

    print("썸네일 이미지 src:")
    for src in images:
        print(src)
