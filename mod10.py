#-------------------------------------------------------------------------------
# Name:        mod10
# Purpose:
#
# Author:      Nag
#
# Created:     29.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

number = input("Назовите число?")
number = int(number)

if number % 10 == 0:
    print("Ваше число " + str(number) + " кратно 10.")
else:
    print("Ваше число " + str(number) + " не кратно 10.")