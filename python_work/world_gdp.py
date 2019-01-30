import json
import pygal
from country_code import get_country_code
from pygal.style import CleanStyle as RBS


# Список заполяется данными
filename = '.\\data\\gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Построение словаря с данными численности населения
cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2015:
        country = gdp_dict['Country Name']
        gdp = int(gdp_dict['Value'])
        code = get_country_code(country)
        if code:
            cc_gdps[code] = gdp

wm_style = RBS()
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World GDP in 2010, by Country'
wm.add('2015', cc_gdps)

wm.render_in_browser()
