from osm.premiershipRugby.oddsPortal.scraper.pageHtml.HtmlParser import parse
from osm.premiershipRugby.oddsPortal.scraper.pageHtml.TagExtractor import tag_extractor


def scrape_results(url):
    """Takes a url, scrapes and parses the html data from it and returns a key: value dictionary of data about
    matches.

    :param url: The url to be scraped
    :return: A key: value dictionary of odds data about individual matches
    """
    # Extracts data in div tags from url
    divs = parse(url)

    # Creates and returns a list of dictionaries of odds information about each match from divs
    return tag_extractor(divs)
