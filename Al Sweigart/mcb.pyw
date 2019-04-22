#! python3
# mcb.pyw - Сохраняет и загружает фрагменты текста
# в буфер обмена.
# Использование: py.exe mcb.pyw save <ключевое слово> -
#               Сохраняет буфер обмена в ключевое слово.
#               py.exe mcb.pyw <ключевое слово> -
#               Загружает ключевое слово в буфер обмена.
#               py.exe mcb.pyw list -
#               Загружает все ключевые слова в буфер обмена.

import shelve, pyperclip, sys


mcbShelf = shelve.open('mcb')

# Сохранение содержимого буфера обмена
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: Сформировать список ключевых слов и загрузить
# TODO: содержимое

mcbShelf.close()
