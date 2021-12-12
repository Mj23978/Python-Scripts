import os
import shutil
import subprocess
from os import path


files = []
errors = []


def file_exist(location: str):
    ext = path.splitext(location)[1]
    if ext == ".mp4" or ext == ".avi" or ext == ".webm" or ext == ".gif":
        files.append(location)


def convert_file(file_name: str, folder_name: str):
    try:
        create_folder(folder_name)
        convert_h265(file_name)
        os.chdir(move_path)
    except Exception as _:
        errors.append(file_name)
        os.chdir(move_path)
        print("Error", file_name)


def create_folder(file_name: str):
    dir_name = path.join(path.abspath('')) + '\\' + file_name
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)


def convert_h265(file_name: str):
  subprocess.run(
      f"ffmpeg -i \"{move_path}\\{file_name}\" -c:v libx265 -crf 28 -preset faster -c:a aac -b:a 128k \"{move_path}\\out\\{file_name}\"")

def main():
    move_path = path.abspath('.')
    tmp_files = os.listdir(move_path)

    for my_file in tmp_files:
        file_exist(my_file)

    return move_path


move_path = main()
print(len(files))

for nfile in files:
    convert_file(nfile, 'out')
