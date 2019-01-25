import json
from country_code import get_country_code


# Список заполяется данными
filename = '.\\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Вывод населения каждой страны за 2010 год.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        code = get_country_code(country_name)
        if code:
            print(code + " : " + population)
        else:
            print('ERROR - ' + country_name)