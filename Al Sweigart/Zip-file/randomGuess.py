
import random

guess = ''
while guess not in ('орел', 'решка'):
    print('Угадайте результат подбрасывания монеты!')
    guess = input('Орел или решка:')
toss = random.randint(0, 1)
if toss == 0:
    toss = 'решка'
else:
    toss = 'орел'
if toss == guess:
    print('Есть!')
else:
    print('Увы! Попробуйте ещё раз!')
    guess = input()
    if toss == 0:
        toss = 'решка'
    else:
        toss = 'орел'
    if toss == guess:
        print('Есть!')
    else:
        print('Нет. Вам действительно не везет в этой игре.')