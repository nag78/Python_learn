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
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
        mcbShelf.pop(sys.argv[2])


elif len(sys.argv) == 2:
    # Формирование списока ключевых слов и загрузка содержимого.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    if sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

mcbShelf.close()
