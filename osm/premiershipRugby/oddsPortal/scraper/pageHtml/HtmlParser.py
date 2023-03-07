import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def parse(url):
    """Scrapes and parses html data from a url and returns div tags that match id of 'tournamentTable'.

    :param url: The url to be scraped
    :return: A ResultSet of div tags
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:

        driver.execute_script(f"window.scrollTo(0, {last_height});")
        time.sleep(1)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

    time.sleep(3)
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, "html.parser")
    divs = soup.find("div", {"class": "flex flex-col px-3 text-sm max-mm:px-0"})

    return divs
