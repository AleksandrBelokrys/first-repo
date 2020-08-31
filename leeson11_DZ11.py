import json


def read_json(filename_with_path):
    with open(filename_with_path, 'r') as json_file:
        data = json.load(json_file)
        print(data)


print(read_json(r"C:\Users\Admin\PycharmProjects\first\first-repo\data.json"))