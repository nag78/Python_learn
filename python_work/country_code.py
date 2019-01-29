from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Возвращает для заданной страны ее код Pygal, состоящий из 2 букв."""
    if country_name == 'Yemen, Rep.':
        country_name = 'Yemen'
    elif country_name == 'Korea, Rep.':
        country_name = 'Korea, Republic of'
    elif country_name == 'Korea, Dem. Rep.':
        country_name = "Korea, Democratic People's Republic of"
    elif country_name == 'Tanzania':
        country_name = 'Tanzania, United Republic of'
    elif country_name == 'Venezuela, RB':
        country_name = 'Venezuela, Bolivarian Republic of'
    elif country_name == 'Vietnam':
        country_name = 'Viet Nam'
    elif country_name == 'Egypt, Arab Rep.':
        country_name = 'Egypt'
    elif country_name == 'Libya':
        country_name = 'Libyan Arab Jamahiriya'
    elif country_name == 'Moldova':
        country_name = 'Moldova, Republic of'
    elif country_name == 'Congo, Rep.':
        country_name = 'Congo'
    elif country_name == 'Congo, Dem. Rep.':
        country_name = 'Congo, the Democratic Republic of the'
    elif country_name == 'Bolivia':
        country_name = 'Bolivia, Plurinational State of'
    elif country_name == 'Iran, Islamic Rep.':
        country_name = 'Iran, Islamic Republic of'
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # Если страна не найдена, вернуть None.
    return None


print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
