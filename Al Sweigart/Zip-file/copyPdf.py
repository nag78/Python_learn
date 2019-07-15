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

        # print('Copy from ...' + str(folderName))
        for subfolder in subfolders:
            # print('Copy from ...' + str(folderName) + str(subfolder))
            continue
        for filename in filenames:
            if filename.endswith('.pdf'):
                dst = os.path.join(target, filename)
                src = os.path.join(folderName, filename)
                print('Copy...' + str(src))
                shutil.copy(src, dst)


copyPdf('D:\\Downloads', 'D:\\PDF')
