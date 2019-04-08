# -*- coding: cp1251 -*-
# passwordCheck.py - Проверяет является ли
# строка в буфере хорошим паролем. Хороший
# пароль не менее 8 символов, содержит
# символы в верхнем и нижнем регистре и не
# менее одной цифры.


import pyperclip
import re


def checkpass(password):
    return len(password) > 8 and all(re.search(p, password) for p in ('[A-Z]',
                                                                      '\d',
                                                                      '[a-z]'))


text = str(pyperclip.paste())
test = checkpass(text)

if test:
    print('Хороший пароль: ' + str(text))
else:
    print('Плохой пароль: ' + str(text))
