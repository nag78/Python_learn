#-------------------------------------------------------------------------------
# Name:        users
# Purpose:
#
# Author:      Nag
#
# Created:     19.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


users = ['nag','bag','tda','z08','kei','admin']


for user in users:
    if user == 'admin':
        print("\nHello " + user.title() + " whould you like to see a status report?")
    else:
        print("Hello " + user.title() + " thank you for logging in again.")

users = []

if users:
    for user in users:
        print ("\nHello " + user.title() + "!")
else:
    print("\nWe need to find some users!")

current_users = ['nag','bag','tda','z08','kei','admin']
new_users = ['bag','z08','KEI', 'z01', 'N08']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Пользователь " + new_user.title() + " есть в списке!")
    else:
        current_users.append(new_user.lower())
        print("Пользователь " + new_user.title() + " добавлен!")
print("Итоговый список:\n")
print(current_users)


numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+"nd")
    elif number == 3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")

