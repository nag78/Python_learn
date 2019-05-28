# -*- coding: cp1251 -*-
# Вывод файлов превышающих 100Мб

import os


def getSizeFile(fldr):

    fldr = os.path.abspath(fldr)

    for folder, subfolders, files in os.walk(fldr):
        for subfolder in subfolders:
            continue

        for file in files:
            path = os.path.join(folder, file)
            if os.path.getsize(path) > 104857600:
                print(str(path) + ' - ' + str((os.path.getsize(path))/1048576) + ' Мб')

getSizeFile('D:\\PDF')