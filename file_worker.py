#csv,  json
from data_former import *
import csv
import json


def find_csv_separator(file_name):
    chunk_for_sniffing = 1000
    sniffer = csv.Sniffer()
    with open(file_name, encoding='UTF-8') as file:
        separator = sniffer.sniff(file.read(chunk_for_sniffing)).delimiter
    return separator


file_name_csv = "database.csv"
file_name_import_csv = "import_data.csv"
file_name_json = "data.json"
# DB_HEADER = ["ID", "Title", "Description", "Date/Time"]
CSV_DELIMITER = ';'


def read_from_csv_file(file_name=file_name_csv):
    '''
    Функция чтения из csv файла (на выходе список словарей)
    '''
    data = []
    with open(file_name, 'r', encoding='UTF-8') as file_csv:
        reader_from_file = csv.DictReader(file_csv, delimiter=CSV_DELIMITER)
        for row in reader_from_file:
            data.append(row)
    return data


def write_to_csv_file(data, file_name=file_name_csv):
    '''
    Функция записи в csv файл (вход -> список списков данных)
    например, data = [["9", "Дело9", "Описание 9", datetime.datetime(2019, 2, 13, 13, 12)],
                      ["10", "Дело10", "Описание 10", datetime.datetime(2020, 6, 9, 12, 0)]]
    '''
    with open(file_name, 'w', encoding='UTF-8') as file_csv:
        writer_to_file = csv.writer(file_csv, delimiter=CSV_DELIMITER)
        writer_to_file.writerow(DB_HEADER)
        for row in data:
            writer_to_file.writerow(row)


def add_to_csv_file(data: list, file_name=file_name_csv):
    '''
    Функция добавления данных (вход -> список списков данных) в csv файл
    например, data = [["9", "Дело9", "Описание 9", datetime.datetime(2019, 2, 13, 13, 12)]]
    '''
    with open(file_name, 'a', encoding='UTF-8') as file_csv:
        writer_to_file = csv.writer(file_csv, delimiter=CSV_DELIMITER)
        for row in data:
            writer_to_file.writerow(row)


def export_from_csv_to_json_file(file_name_from=file_name_csv, file_name_to=file_name_json):
    '''
    Функция экспорта из csv файла в json файл 
    '''
    data = read_from_csv_file(file_name_from)
    with open(file_name_to, 'w', encoding='UTF-8') as file_json:
        json.dump(data, file_json, ensure_ascii=False)


def read_from_json_file(file_name=file_name_json):
    '''
    Функция чтения из json файла (на выходе список словарей)
    '''
    #data = read_from_csv_file(file_name)
    with open(file_name, 'r', encoding='UTF-8') as file_json:
        data = json.load(file_json)
    return data


def import_from_json_to_csv_file(file_name_from=file_name_json, file_name_to=file_name_import_csv):
    '''
    Функция импорта из json в csv файл 
    '''
    data_dict = read_from_json_file(file_name_from)
    data_list = []
    for i in range(len(data_dict)):
        data_list.append(from_dict_to_value_list(data_dict[i]))
    write_to_csv_file(data_list, file_name_to)


