#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nag
#
# Created:     29.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
prompt_1 = "\nВведите первое число: "
prompt_1 += "\nдля выхода введите 'q'"
prompt_2 = "\nВведите второе чичло: "
prompt_2 += "\nдля выхода введите 'q'"

while True:
    num_1 = input(prompt_1)
    if num_1 == 'q':
        break
    num_2 = input(prompt_2)
    if num_2 == 'q':
        break
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        sum = num_1 + num_2
    except ValueError:
        print("Введеные символы не являются числом.")
    print("Сумма: " + str(sum))

