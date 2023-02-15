import datetime

def delete_extra_spaces(string_original):
    string_original = string_original.strip()
    return string_original


def check_symbol_digit(symbol):
    if symbol.isdigit() or symbol == "":
        return True
    else:
        return False


def check_data_empty_all(*data):
    for item in data:
        if item != "":
            return True
    return False


def check_data_empty_at_least_one(*data):
    for item in data:
        if item == "":
            return False
    return True

def  check_date_values(*data):
    format = "%Y-%m-%d"
    date_str = "-".join(data)

    result = True
 
    try:
        result = bool(datetime.datetime.strptime(date_str, format))
    except ValueError:
        result = False
    
    return result


