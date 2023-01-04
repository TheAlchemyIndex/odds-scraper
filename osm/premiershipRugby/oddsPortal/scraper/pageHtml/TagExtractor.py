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
    home_odds = ""

    # Gets main table of data
    table = divs.find("table", {"class": "table-main"})
    # Gets 'tbody' tag from table
    t_body = table.find("tbody")

    for tr in t_body:
        # List to hold the odds for draws and away wins
        draw_away_odds = []
        # Gets date
        if tr['class'] == ['center', 'nob-border']:
            date = tr.text
        elif tr['class'] == ['odd', 'deactivate']:
            for td in tr:
                # Gets team names
                if td['class'] == ['name', 'table-participant']:
                    teams = td.text.split(" - ")
                    team1 = teams[0]
                    team2 = teams[1]
                # Gets home odds
                elif td['class'] == ['result-ok', 'odds-nowrp']:
                    home_odds = td.text
                # Gets draw and away odds
                elif td['class'] == ['odds-nowrp']:
                    draw_away_odds.append(td.text)
            match_odds = {"date": date, "team1": team1, "team2": team2, "homeOdds": home_odds,
                          "drawOdds": draw_away_odds[0], "awayOdds": draw_away_odds[1]}
            odds.append(match_odds)
        elif tr['class'] == ['deactivate']:
            for td in tr:
                # Gets team names
                if td['class'] == ['name', 'table-participant']:
                    teams = td.text.split(" - ")
                    team1 = teams[0]
                    team2 = teams[1]
                # Gets home odds
                elif td['class'] == ['result-ok', 'odds-nowrp']:
                    home_odds = td.text
                # Gets draw and away odds
                elif td['class'] == ['odds-nowrp']:
                    draw_away_odds.append(td.text)
            match_odds = {"date": date, "team1": team1, "team2": team2, "homeOdds": home_odds,
                          "drawOdds": draw_away_odds[0], "awayOdds": draw_away_odds[1]}
            odds.append(match_odds)

    print(odds)
    return odds
