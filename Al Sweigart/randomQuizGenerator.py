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
    # Создание файлов билетов.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answer%s.txt' % (quizNum +
                         1), 'w')
    # Запись заголовков билетов.
    quizFile.write('Имя:\n\nДата:\n\nКурс:\n\n')
    quizFile.write((' ' * 15
                    ) + 'Проверка знания столиц штатов (Билет %s)' % (
                    quizNum + 1))
    quizFile.write('\n\n')

    # Перемешивание порядка следования столиц штатов
    states = list(capitals.keys())
    random.shuffle(states)

# Организация цикла по всем 50 штатам,
    # создание вопроса для каждого из них.
for questionNum in range(50):
    # Получение правильных и неправильных вопросов и ответов
    correctAnswer = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

    # TODO: Записать варианты вопросов и ответов в файл билета
    # TODO: Записать ключ ответа в файл.
