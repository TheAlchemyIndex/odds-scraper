import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def parse(url):
    """Scrapes and parses html data from a url and returns div tags that match id of 'tournamentTable'.

    :param url: The url to be scraped
    :return: A ResultSet of div tags
    """
    # Get data from url
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, "html.parser")
    divs = soup.find("div", {"id": "tournamentTable"})

    return divs
