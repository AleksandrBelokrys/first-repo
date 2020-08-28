import json
import csv
from random import choice, randint, random, choices
from string import ascii_letters, digits, punctuation, ascii_lowercase


def write_txt(file):
    string_length = randint(100, 1000)
    chars = ascii_letters + digits + punctuation + ' '
    string_list = choices(chars, k=string_length)

    positions = set()
    while len(positions) < 9:
        position = randint(0, string_length)
        positions.add(position)
    for position in positions:
        string_list.insert(position, '\n')
    string = ''.join(string_list)

    with open(file, 'w') as f:
        f.write(string)

    return string


def write_json(file):
    num_of_keys = randint(5, 20)
    keys = set()
    values = []
    while len(keys) < num_of_keys:
        key = ''.join(choices(ascii_lowercase, k=5))
        keys.add(key)

    my_dict = dict.fromkeys(keys)

    for key in keys:
        type_of_value = choice(['int', 'float', 'bool'])

        if type_of_value == 'int':
            my_choice = randint(-100, 100)
        elif type_of_value == 'float':
            my_choice = random()
        else:
            my_choice = choice([True, False])

        my_dict[key] = my_choice
    with open(file, 'w') as f:
        json.dump(my_dict, f, indent=2)

    return my_dict


def write_csv(file):
    n = randint(3, 10)
    m = randint(3, 10)
    data = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            data[i][j] = choice([0, 1])
    with open(file, 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
    return data


def file_writer(filename_with_path):
    ext = filename_with_path.rsplit(".", 1)[-1]
    if ext == "txt":
        data = write_txt(filename_with_path)
    elif ext == "json":
        data = write_json(filename_with_path)
    elif ext == "csv":
        data = write_csv(filename_with_path)
    else:
        raise Exception("Unsupported file format!")
    return data









