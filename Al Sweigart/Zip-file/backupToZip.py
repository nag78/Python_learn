# -*- coding: cp1251 -*-

import zipfile
import os


def backupToZip(folder):
    # Создание резервной копии всего
    # содержимого папки folder
    # в виде Zip файла

    # Определяем что задан абсолютный путь
    folder = os.path.abspath(folder)

    # Определяем, какое имя должен использо-
    # вать этот код, исходя из имен уже
    # существующих файлов
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Создать zip file
    print('Создается файл %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Обойти все дерево папки и
    # сжать файлы, содержащиеся в
    # каждой папке.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Добавление файлов из папки %s...' % (foldername))
        # Добавить в ZIP-файл текущую папку
        backupZip.write(foldername)
        # Добавить в ZIP-файл все файлы из этой папки
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Готово')


backupToZip('C:\\delicious')
