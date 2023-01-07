from mos.premiershipRugby.oddsPortal.scraper.writers.FileWriter import write_to_individual_files


def write_all_odds(first_season_start, first_season_end, last_season):
    """Writes match odds data to csv file.

    :param first_season_start: The start year of the first season to be scraped and written to csv (e.g., 2010)
    :param first_season_end: The second year of the first season to be scraped and written to csv (e.g., 2011)
    :param last_season: The second year of the last season to be scraped and written to csv (e.g., 2023)
    """
    write_to_individual_files(first_season_start, first_season_end, last_season)

