from os import listdir, mkdir, rename
from os.path import isfile, join, isdir, dirname, basename



# 1-я функция
def name_and_folder_path(path):
    filename = basename(path)
    folder_path = dirname(path)
    return filename, folder_path


# 2-я функция
def file_list(path):
    filename = [file for file in listdir(path) if isfile(join(path, file))]
    return filename


# 3-я функция
def path_dict(path):
    my_dict = {}
    files = [file for file in listdir(path) if isfile(join(path, file))]
    folders = [file for file in listdir(path) if isdir(join(path, file))]
    my_dict["files"] = files
    my_dict["folders"] = folders
    return my_dict


# 4-я функция
def create_folder(path):
    for file in listdir(path):
        if isdir(join(path, file)):
            rename(file, file + "_tmp")
        else:
            mkdir("tmp")













