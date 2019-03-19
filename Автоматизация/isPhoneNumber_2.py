# -*- encoding: cp1251 -*-
from re import compile as re_cmpl

message = '''
            Позвони мне завтра по номеру 415-555-1011.
            415-555-9999 - это телефонный номер моего офиса.
          '''
phoneNumRegx = re_cmpl(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegx.findall(message)

for n in mo:
    print('Найден номер: ' + str(n))
