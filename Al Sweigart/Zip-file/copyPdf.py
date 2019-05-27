# -*- coding: cp1251 -*-


import os
import shutil


def copyPdf(source, target):
    # Копирование файлов pdf из
    # папки source в target

    # Определяем, что заданы
    # абсалютные пути
    source = os.path.abspath(source)
    target = os.path.abspath(target)

    # Обход папки source
    for folderName, subfolders, filenames in os.walk(source):

        print(str(folderName))
        for filename in filenames:
            dst = os.path.join(target, filename)
            src = os.path.join(source, filename)
            print('Copy...' + str(src)
            shutil.copy(src, dst)


copyPdf('C:\\1\\', 'C:\\2\\')