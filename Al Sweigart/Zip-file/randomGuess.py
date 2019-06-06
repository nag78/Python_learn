
import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Начало программы')

def brosok(guess, toss):
    '''Функция проверки результата'''
    logging.debug('Начало подпрограммы.')
    if guess == 'решка':
        guess = 0
    else:
        guess = 1
    logging.debug('guess = ' + str(guess) + ' toss = ' + str(toss))
    if toss == guess:
        return True
    else:
        return False


guess = ''
while guess not in ('орел', 'решка'):
    print('Угадайте результат подбрасывания монеты!')
    guess = input('Орел или решка:')
    logging.debug('guess = ' + str(guess))
toss = random.randint(0, 1)
logging.debug('toss = ' + str(toss))
if brosok(guess, toss):
    print('Есть!')
else:
    print('Увы! Попробуйте ещё раз!')
    guess = input()
    if brosok(guess, toss):
        print('Есть!')
    else:
        print('Нет. Вам действительно не везет в этой игре.')
logging.debug('Конец программы.')
