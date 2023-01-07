def odds_formatter(odds_data):
    """Reformats fractional odds into decimal odds.

    :param odds_data: Fractional odds for a match
    :return: Odds for a match in decimal format
    """
    # "-" means no potential return, so 1 is returned
    if odds_data == "-":
        return 1
    else:
        split_odds = odds_data.split("/")
        decimal_odds = (int(split_odds[0]) / int(split_odds[1])) + 1
        return decimal_odds
