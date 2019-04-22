''' Создает эзаменационные билеты с вопросами
 и ответами, расположенными в случайном порядке,
 вместе с ключами ответов.'''

import random
# Данные билетаю. Ключи - названия штатов,
# а значения - столицы.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
            'Arizona': 'Phoenix', 'Arkanzas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delawer': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu', 'Ideho': 'Boise',
            'Illinois': 'Sprigfield', 'Indiana': 'Indianapolice',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Luisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolice',
            'Massachussetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jafferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hempshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Caralina': 'Raleigh', 'North Dacota': 'Bismark',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Colambia',
            'South Dacota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Генерация 35 файлов билетов
for quizNum in range(35):
    # TODO: Создать файлы билетов и ключей ответов

    # TODO: Перемешать порядок следования штатов

    # TODO: Организовать цикл по всем 50 штатам,
    # TODO: создавая вопрос для каждого из них.
