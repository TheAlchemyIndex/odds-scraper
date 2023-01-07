from mos.premiershipRugby.oddsPortal.scraper import ScrapingModule


def main():
    ScrapingModule.write_all_odds(2008, 2009, 2023)


if __name__ == "__main__":
    main()
