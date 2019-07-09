# -*- coding: utf8 -*-
#! python3
# lucky.py - Открывает несколько результатов
# поиска с помощью Google.

import requests
import sys
import webbrowser
import bs4


print('Гуглим...') # отображается при загрузке
                   # гугла
res = requests.get('http://google.com/search?q=' +
                    ' '.join(sys.argv[1:]))
res.raise_for_status()


# Извлечь перввые несколько найденных ссылок
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Открыть отдельную вкладку для каждого результата
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('herf'))