import csv
from country_code import get_country_code
import pygal
from pygal.style import LightGreenStyle as ST


# Чтение файла
fname = ".\\csv\\forests_area.csv"
# y = '2018'
# prompts = 'Выведите год от 1960 до 2018 включительно'
# row_count = [range(1960, 2018)]
forestes = {}
with open(fname) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        country = row[0]
        try:
            forest = round(float(row[60]), 2)
        except ValueError:
            print("error data")
        else:
            code = get_country_code(country)
            if code:
                forestes[code] = forest
# print(forestes)
wm_style = ST()
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Forest area (% of land area) in 2018, by Country'
wm.add('2018', forestes)

wm.render_in_browser()
