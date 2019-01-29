import json
import pygal
from country_code import get_country_code
from pygal.style import CleanStyle as RBS


# Список заполяется данными
filename = '.\\data\\gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)

# Построение словаря с данными численности населения
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population
        else:
            print(country)
            # Проверка количества стран на каждом уровне
            # print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RBS()
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_in_browser()
