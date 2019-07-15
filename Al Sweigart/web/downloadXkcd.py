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

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # Найти URL- адрес изображения комикса
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалось найти изображение комикса.')
    else:
        comicUrl = comicElem[0].get('src').strip("http://")
        comicUrl="http://"+comicUrl
        if 'xkcd' not in comicUrl:
            comicUrl=comicUrl[:7]+'xkcd.com/'+comicUrl[7:]

        # Загрузить картинку в папке ./xkcd.
        print('Загружается изображение %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Сохранение изображений в папке ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #Получить URL-адрес кнопки Prev.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Готово!')