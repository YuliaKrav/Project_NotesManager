
import datetime


DB_HEADER = ["ID", "Title", "Description", "Date/Time"]


def get_datetime_now():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime('%Y-%m-%d %H:%M:%S')

def get_datetime_from_string(data_str):
    return datetime.datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')

def from_dict_to_value_list(dict):
    result_list = []
    for header in DB_HEADER:
        result_list.append(dict[header])
    return result_list
