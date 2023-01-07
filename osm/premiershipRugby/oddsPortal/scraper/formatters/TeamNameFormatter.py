def team_name_formatter(team_name_data):
    """Takes team information and reformats it.

    :param team_name_data: Team name to be formatted
    :return: A reformatted version of the team name
    """

    if team_name_data == "Bath Rugby":
        return "Bath"
    elif team_name_data == "Bristol Bears":
        return "Bristol"
    elif team_name_data == "Exeter Chiefs":
        return "Exeter"
    elif team_name_data == "Leeds Carnegie":
        return "Leeds"
    elif team_name_data == "Leicester Tigers":
        return "Leicester"
    elif team_name_data == "Gloucester Rugby":
        return "Gloucester"
    elif team_name_data == "Newcastle Falcons":
        return "Newcastle"
    elif team_name_data == "Northampton Saints":
        return "Northampton"
    elif team_name_data == "Sale Sharks":
        return "Sale"
    elif team_name_data == "London Wasps":
        return "Wasps"
    elif team_name_data == "Worcester Warriors":
        return "Worcester"
    elif team_name_data == "Yorkshire":
        return "Leeds"
    else:
        return team_name_data
