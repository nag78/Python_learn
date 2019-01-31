import csv
from country_code import get_country_code
import pygal
from pygal.style import BlueStyle as ST


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
                # Группировка по %
                cc_fos_1, cc_fos_2, cc_fos_3, cc_fos_4 = {}, {}, {}, {}
                for cc, fos in forestes.items():
                    if fos < 5:
                        cc_fos_1[cc] = fos
                    elif fos < 25:
                        cc_fos_2[cc] = fos
                    elif fos < 50:
                        cc_fos_3[cc] = fos
                    else:
                        cc_fos_4[cc] = fos
# print(forestes)
wm_style = ST()
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Forest area (% of land area) in 2018, by Country'
wm.add('0 - 5 %', cc_fos_1)
wm.add('5 - 25 %', cc_fos_2)
wm.add('25 - 50 %', cc_fos_3)
wm.add('> 50 %', cc_fos_4)

wm.render_in_browser()
