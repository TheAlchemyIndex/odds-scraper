import csv


def write_to_csv(odds_data, file_name, field_names):
    """Writes data to csv file.

    :param odds_data: Match odds data to be written to csv file
    :param file_name: The name of the file to be written to
    :param field_names: The column names to use when writing to the csv file
    """
    with open(file_name, "w", encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(odds_data)
