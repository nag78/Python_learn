#! python3
# downloadXkcd.py - Загружает все комиксы с XKCD.

import request
import os
import bs4


url = 'http://xkcd.com'
os.mkdir('xkcd', exist_ok=True)

while not url.endswith('#'):
    #TODO: Загрузить страницу
    #TODO: Найти URL- адрес изображения комикса
    #TODO: Сохранить картинку в папке ./xkcd.
    #TODO: Получить URL-адрес кнопки Prev
print('Готово!')