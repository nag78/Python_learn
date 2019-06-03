# -*- coding: cp1251 -*-
def spam():
    bacon()

def bacon():
    raise Exception('Это сообщение об ошибке.')

spam()