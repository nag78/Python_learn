
import random

def brosok(guess, toss):
    '''Функция проверки результата'''
    if guess == 'решка':
        guess = 0
    else:
        guess = 1
    if toss == guess:
        return True
    else:
        return False


guess = ''
while guess not in ('орел', 'решка'):
    print('Угадайте результат подбрасывания монеты!')
    guess = input('Орел или решка:')
toss = random.randint(0, 1)
if brosok(guess, toss):
    print('Есть!')
else:
    print('Увы! Попробуйте ещё раз!')
    guess = input()
    if brosok(guess, toss):
        print('Есть!')
    else:
        print('Нет. Вам действительно не везет в этой игре.')



# TODO: Дописать логгирование