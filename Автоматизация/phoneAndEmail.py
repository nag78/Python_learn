# -*- coding: cp1251 -*-
#! python3
# phoneAndEmail.py - Находит телефонные номера и 
# адреса электронной почты в буфере обмена


import pyperclip, re


phoneRegex = re.compile(r'''(
                             (\d{3}|\(\d{3}\))?                          # территориальный код
                             (\s|-|\.)?                                  # разделитель
                             (\d{3})                                     # первые 3 цифры
                             (\s|-|\.)                                   # разделитель
                             (\d{4})                                     # последние 4 цыфры
                             (\s*(ext|x|ext.)\s*(\d{2,5}))?              # добавочный номер
                            )''', re.VERBOSE)


# Создание регулярного выражения для адресов электронной почты.
emailRegex = re.compile(r'''(
                             [a-zA-z0-9._%+-]+                           # имя пользователя
                             @                                           # символ @
                             [a-zA-z0-9.-]+                              # доменное имя
                             (\.[a-zA-Z](2,4))                           # Домен верхнего уровня
                            )''', re.VERBOSE)

# Поиск соответствия в тексте, содержащемся в буфере обмена.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Копировать результат в буфер обмена.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса email не найдены.')