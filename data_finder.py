import data_former


def filter_data(date1, date2, data_notes):
    filtered_data = []
    for note in data_notes:
        date_time = data_former.get_datetime_from_string(note[3])
        if date1 <= date_time <= date2:
            filtered_data.append(note)
    return filtered_data