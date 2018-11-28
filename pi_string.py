#-------------------------------------------------------------------------------
# Name:        pi_string
# Purpose:
#
# Author:      Nag
#
# Created:     28.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    birthday = input("Enter your birthday, in the form ddmmyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Yours birhday does not appear in the first million digits of pi")


