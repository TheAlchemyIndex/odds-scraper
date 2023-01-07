from mos.premiershipRugby.oddsPortal.constants import Columns
from mos.premiershipRugby.oddsPortal.scraper.seasons.SeasonScraper import scrape_results
from mos.premiershipRugby.oddsPortal.scraper.writers.CsvWriter import write_to_csv

# Constant list for field names
FIELD_NAMES = [Columns.DATE, Columns.TEAM1_NAME, Columns.TEAM2_NAME, Columns.TEAM1_ODDS, Columns.DRAW_ODDS,
               Columns.TEAM2_ODDS]

AVIVA_SEASONS = ["2008-2009", "2009-2010", "2010-2011", "2011-2012", "2012-2013", "2013-2014", "2014-2015",
                 "2015-2016", "2016-2017", "2017-2018"]


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
        odds_data = []

        # Url is different depending on what season is used
        if season in AVIVA_SEASONS:
            url = "https://www.oddsportal.com/rugby-union/england/aviva-premiership-rugby-" + season + "/results/"
        elif season == "2022-2023":
            url = "https://www.oddsportal.com/rugby-union/england/premiership-rugby/results/"
        else:
            url = "https://www.oddsportal.com/rugby-union/england/premiership-rugby-" + season + "/results/"

        file_name = "data/Odds" + " - " + str(first_season_start) + "-" + str(first_season_end) + ".csv"

        for page in range(3):
            try:
                if page + 1 == 1:
                    odds_data = odds_data + scrape_results(url)
                else:
                    odds_data = odds_data + scrape_results(url + "#/page/" + str(page + 1))
            except KeyError:
                continue

        write_to_csv(odds_data, file_name, FIELD_NAMES)
        first_season_start += 1
        first_season_end += 1
