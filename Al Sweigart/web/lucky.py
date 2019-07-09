#! python3
# lucky.py - Открывает несколько результатов поиска
# с помощью Google.

import requests
import sys
import webbrowser
import bs4


print('Гуглим...') # отображается при загрузке гугла
res = requests.get('http://google.com/search?q=' +
                    ' '.join(sys.argv[1:]))
res.raise_for_status()


# TODO: Извлечь перввые несколько найденных ссылок

# TODO: ОТкрыть отдельную вкладку для каждого результата