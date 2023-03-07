from osm.premiershipRugby.oddsPortal.scraper.formatters.DateFormatter import date_formatter
from osm.premiershipRugby.oddsPortal.scraper.formatters.OddsFormatter import odds_formatter
from osm.premiershipRugby.oddsPortal.scraper.formatters.TeamNameFormatter import team_name_formatter


def tag_extractor(divs):
    """Loops through a ResultSet of div tags and returns odds data about matches.

    :param divs: A ResultSet of div tags to be looped through
    :return: A key: value dictionary of odds data about matches
    """
    # Empty list to contain data about each match
    odds = []

    # Gets rows of match data from divs
    event_rows = divs.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})

    date = ""

    for event in event_rows:
        teams = []
        match_odds = []
        team1 = ""
        team2 = ""
        event_data = event.find_all("div")
        for div in event_data:
            if div.has_attr('class'):

                # Gets date
                if div['class'] == ['w-full', 'text-xs', 'font-normal', 'leading-5', 'text-black-main', 'font-main']:
                    date = date_formatter(div.text)
                elif div['class'] == ['relative', 'w-full', 'flex-col', 'flex', 'text-xs', 'leading-[16px]',
                                      'min-w-[0]',
                                      'gap-1', 'next-m:!flex-row', 'next-m:!gap-2', 'justify-center']:

                    for tag in div:
                        if tag.text != "–":
                            teams.append(tag.text)
                    team1 = team_name_formatter(teams[0])
                    team2 = team_name_formatter(teams[1])

                elif div['class'] == ['flex-center', 'flex-col', 'gap-1', 'pt-1', 'pb-1', 'border-l',
                                      'border-black-main', 'border-opacity-10', 'min-w-[60px]']:
                    match_odds.append(div.text)

        match_odds = {"date": date, "team1Name": team1, "team2Name": team2,
                      "team1Odds": odds_formatter(match_odds[0]),
                      "drawOdds": odds_formatter(match_odds[1]),
                      "team2Odds": odds_formatter(match_odds[2])}
        odds.append(match_odds)

    print(odds)
    return odds
