import datetime


def date_formatter(date_data):
    """Takes a date, reformats it and returns it.

    :param date_data: Date information about a match
    :return: A reformatted version of the date
    """
    date_replace = date_data.replace("1X2B's", "").replace("- Play Offs", "").replace("Play Offs", "")\
        .replace("Yesterday, ", "").replace("Today, ", "").strip()

    # Dates from yesterday or today are missing the year value, so this is appended if found using try except
    try:
        date = datetime.datetime.strptime(date_replace, '%d %b %Y').strftime('%d/%b/%Y')
    except ValueError:
        current_year = datetime.datetime.now().year
        date = datetime.datetime.strptime(date_replace, '%d %b').strftime('%d/%b/') + str(current_year)

    return date
