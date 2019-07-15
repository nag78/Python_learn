# -*- coding: cp1251 -*-
#! python3
# downloadXkcd.py - Загружает все комиксы с XKCD.

import requests
import os
import bs4


url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print('Загоужается страница %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    #TODO: Найти URL- адрес изображения комикса
    #TODO: Сохранить картинку в папке ./xkcd.
    #TODO: Получить URL-адрес кнопки Prev.

print('Готово!')