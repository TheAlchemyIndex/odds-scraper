from osm.premiershipRugby.oddsPortal.scraper.seasons.SeasonScraper import scrape_results
from osm.premiershipRugby.oddsPortal.scraper.writers.CsvWriter import write_to_csv

# Constant list for field names
FIELD_NAMES = ["date", "team1", "team2", "homeOdds", "drawOdds", "awayOdds"]


def write_to_individual_files(first_season_start, first_season_end, last_season):
    """Writes match odds data to individual csv files for each season.

    :param first_season_start: The start year of the first season to be scraped and written to csv (e.g., 2010)
    :param first_season_end: The second year of the first season to be scraped and written to csv (e.g., 2011)
    :param last_season: The second year of the last season to be scraped and written to csv (e.g., 2023)
    """
    # Loop continues until last_season_end is reached
    while first_season_end <= last_season:
        season = str(first_season_start) + "-" + str(first_season_end)
        url = ""

        # Url is different depending on what season is used
        if (season == "2014-2015") | (season == "2015-2016") | (season == "2016-2017") | (season == "2017-2018"):
            url = "https://www.oddsportal.com/rugby-union/england/aviva-premiership-rugby-" + season + "/results/"
        elif season == "2022-2023":
            url = "https://www.oddsportal.com/rugby-union/england/premiership-rugby/results/"
        else:
            url = "https://www.oddsportal.com/rugby-union/england/premiership-rugby-" + season + "/results/"

        file_name = "Odds" + " - " + str(first_season_start) + "-" + str(first_season_end) + ".csv"

        write_to_csv(scrape_results(url), file_name, FIELD_NAMES)
        first_season_start += 1
        first_season_end += 1
