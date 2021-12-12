from PIL import Image
from os import path
import shutil
import cairosvg
import os

files = []
errors = []


def FileExist(location):
    ext = path.splitext(location)[1]
    if ext == ".svg":
        files.append(location)


def ConvertSVG(fileName, folderName):
    try:
        createFolder(folderName)
        cairosvg.svg2png(url=convertPath + '\\' +
                         fileName, write_to=f'{fileName[:-4]}.png')
        os.chdir(convertPath)
    except Exception as e:
        errors.append(fileName)
        os.chdir(convertPath)
        print("SVG Error", e)


def ConvertICO(fn):
    try:
        filename = r'' + fn
        img = Image.open(convertPath + '\\Output\\' + filename)
        img.save('logo.ico')
    except Exception as e:
        errors.append(fn)
        print("Error", e)


def createFolder(fileName):
    dir = path.join(path.abspath('')) + '\\' + fileName
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)


def main():
    convertPath = path.abspath('.')
    tmpFiles = os.listdir(convertPath)

    for myFile in tmpFiles:
        FileExist(myFile)

    return convertPath


convertPath = main()
print(files)


for nFile in files:
    # print(convertPath + '\\' + nFile)
    ConvertSVG(nFile, "Output")


ConvertICO(files[0])
