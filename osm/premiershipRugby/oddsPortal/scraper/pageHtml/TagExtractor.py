from mos.premiershipRugby.oddsPortal.scraper.formatters.DateFormatter import date_formatter
from mos.premiershipRugby.oddsPortal.scraper.formatters.OddsFormatter import odds_formatter
from mos.premiershipRugby.oddsPortal.scraper.formatters.TeamNameFormatter import team_name_formatter


def tag_extractor(divs):
    """Loops through a ResultSet of div tags and returns odds data about matches.

    :param divs: A ResultSet of div tags to be looped through
    :return: A key: value dictionary of odds data about matches
    """
    # Empty list to contain data about each match
    odds = []

    date = ""
    team1 = ""
    team2 = ""

    # Gets main table of data
    table = divs.find("table", {"class": "table-main"})
    # Gets 'tbody' tag from table
    t_body = table.find("tbody")

    for tr in t_body:
        # List to hold the odds for the match
        match_odds = []
        # Gets date
        if tr['class'] == ['center', 'nob-border']:
            date = date_formatter(tr.text)
        elif tr['class'] == ['odd', 'deactivate']:
            for td in tr:
                # Gets team names
                if td['class'] == ['name', 'table-participant']:
                    teams = td.text.split(" - ")
                    team1 = team_name_formatter(teams[0])
                    team2 = team_name_formatter(teams[1])
                # Gets match odds
                elif (td['class'] == ['result-ok', 'odds-nowrp']) | (td['class'] == ['odds-nowrp']):
                    match_odds.append(td.text)
            match_odds = {"date": date, "team1Name": team1, "team2Name": team2,
                          "team1Odds": odds_formatter(match_odds[0]),
                          "drawOdds": odds_formatter(match_odds[1]),
                          "team2Odds": odds_formatter(match_odds[2])}
            odds.append(match_odds)
        elif tr['class'] == ['deactivate']:
            for td in tr:
                # Gets team names
                if td['class'] == ['name', 'table-participant']:
                    teams = td.text.split(" - ")
                    team1 = team_name_formatter(teams[0])
                    team2 = team_name_formatter(teams[1])
                # Gets match odds
                elif (td['class'] == ['result-ok', 'odds-nowrp']) | (td['class'] == ['odds-nowrp']):
                    match_odds.append(td.text)
            match_odds = {"date": date, "team1Name": team1, "team2Name": team2,
                          "team1Odds": odds_formatter(match_odds[0]),
                          "drawOdds": odds_formatter(match_odds[1]),
                          "team2Odds": odds_formatter(match_odds[2])}
            odds.append(match_odds)

    return odds
