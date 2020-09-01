import json
import re

# Функция 1


def read_json(filename_with_path):
    with open(filename_with_path, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data

# Функция2


def sort_by_surname(filename_with_path):
    data = read_json(filename_with_path)

    def last_word(string):
        # поиск последнего слова в рядке
        pattern = re.compile(r'\w+$')
        word = pattern.findall(string)[0]
        return word

    data.sort(key=lambda item: last_word(item.get('name')))
    return data

# Функция 3


def sort_by_date_of_death(filename_with_path):
    data = read_json(filename_with_path)

    # поиск даты с BC.
    pattern_bs = re.compile(r'(\d+) .{2,3}$')

    # поиск даты без BC.
    pattern = re.compile(r'(\d+).?$')
    years_with_bc = []
    years_without_bc = []

    for dict_item in data:
        if pattern_bs.findall(dict_item['years']):

            years_with_bc.append(dict_item)
        else:

            years_without_bc.append(dict_item)

    def find_year(re_pattern, string):

        year = re_pattern.findall(string)[0]

        return int(year)

    years_with_bc.sort(key=lambda item: find_year(pattern_bs, item.get('years')), reverse=True)

    years_without_bc.sort(key=lambda item: find_year(pattern, item.get('years')))

    data = years_with_bc
    for dict_item in years_without_bc:
        data.append(dict_item)

        return data

# Функция 4


def sort_by_word_count(filename_with_path):

    data = read_json(filename_with_path)

    def find_len(string):
        pattern = re.compile(r'\w+')
        words = pattern.findall(string)

        length = len(words)
        return length

    data.sort(key=lambda item: find_len(item.get('text')))

    return data


print(sort_by_date_of_death("data.json"))