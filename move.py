from os import path
import shutil
import os

files = []
errors = []


def file_exist(location):
    ext = path.splitext(location)[1]
    if ext == ".png" or ext == ".jpg" or ext == ".mp4" or ext == ".gif":
        files.append(location)


def move_file(file_name, folder_name):
    try:
        create_folder(folder_name)
        shutil.move(move_path + '\\' + file_name, move_path +
                    '\\' + folder_name + '\\' + file_name)
        os.chdir(move_path)
    except Exception as _:
        errors.append(file_name)
        os.chdir(move_path)
        print("Error", file_name)


def create_folder(file_name):
    dir_name = path.join(path.abspath('')) + '\\' + file_name
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)


def main():
    move_path = path.abspath('.')
    tmp_files = os.listdir(move_path)

    for my_file in tmp_files:
        file_exist(my_file)

    return move_path


move_path = main()
print(len(files))

for nfile in files:
    move_file(nfile, 'Pictures')
