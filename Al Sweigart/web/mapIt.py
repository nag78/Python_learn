# -*- coding: cp1251 -*-
#! python3
# mapIt.py - Запускает карту в браузере, извлекая почтовый адрес 
# из командной строки или буфера обмена.


import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    # Получение адреса из команндной строки
    address = ' '.join(sys.argv[1:])
else:
    # Получение адреса из буфера обмена.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
