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

        # TODO: Обойти все дерево папки и
        # сжать файлы, содержащиеся в
        # каждой папке.

