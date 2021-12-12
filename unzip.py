import zipfile
import rarfile
from os import path
import os

rarfile.UNRAR_TOOL = "UnRAR.exe"
files = []
errors = []


def FileExist(location):
    ext = path.splitext(location)[1]
    if ext == ".rar" or ext == ".zip":
        files.append(location)


def UnzipFile(fileName):
    ext = path.splitext(fileName)[1]
    if ext == '.zip':
        try:
            createFolder(fileName)
            with zipfile.ZipFile(compressPath + '\\' + fileName, 'r') as zip_ref:
                zip_ref.extractall(os.getcwd())
            os.chdir(compressPath + '\\Unzip')
            print("Zip", fileName)
        except:
            errors.append(fileName)
            os.chdir(compressPath + '\\Unzip')
            print("Error", fileName)

    elif ext == '.rar':
        try:
            createFolder(fileName)
            with rarfile.RarFile(compressPath + '\\' + fileName, 'r') as rar_ref:
                rar_ref.extractall(os.getcwd())
            os.chdir(compressPath + '\\Unzip')
            print("Rar", fileName)
        except:
            errors.append(fileName)
            os.chdir(compressPath + '\\Unzip')
            print("Error", fileName)

    else:
        print("None")


def createFolder(fileName):
    dir = path.join(path.abspath('')) + '\\' + fileName
    if not os.path.exists(dir):
        os.mkdir(dir)
    else:
        print('Existed', fileName)
    os.chdir(dir)


def main():
    compressPath = path.abspath('..')
    tmpFiles = os.listdir(compressPath)

    for myFile in tmpFiles:
        FileExist(myFile)

    return compressPath

    # for nFile in files:
    # UnzipFile(nFile, compressPath)


compressPath = main()
print(len(files))

for nFile in files:
    UnzipFile(nFile)

print("Errors", errors)


# UnzipFile("00-main-files_NWExYjA0Y2U3YTQ4NWQwMDNkOGU2ZDNh.zip")
# UnzipFile("Carnaval Flat Illustration Set.rar")


# createFolder('Hello')
# try:
#     createFolder("Hello")
#     with rarfile.RarFile("d:\\ui8" + "\\Carnaval Flat Illustration Set.rar", 'r') as rar_ref:
#         rar_ref.extractall(os.getcwd())
#     with zipfile.ZipFile("d:\\ui8" + "\\cobank-banking-finance-and-crypto-wallet-app-ui-kit_NWExYjA0Y2U3YTQ4NWQwMDNkOGU2ZDNh.zip", 'r') as zip_ref:
#         zip_ref.extractall(os.getcwd())
# except:
#     print("Error")
