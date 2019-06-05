# -*- coding: cp1251 -*-
import logging


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -%(message)s')
logging.debug('Начало программы')

def factorial(n):
    logging.debug('Начало factoriala(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = ' + str(i) + ', total = ' + str(total))
        logging.debug('Конец факториала (%s)' % (n))
    return total


print(factorial(8))
logging.debug('Конец программы')
