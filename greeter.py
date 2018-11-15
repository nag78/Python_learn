#-------------------------------------------------------------------------------
# Name:        greeter
# Purpose:
#
# Author:      Nag
#
# Created:     26.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##name = input("Please enter your name: ")
##print("Hello, " + name + "!")
##
##prompt = "If you tell us who you are, we can personalize the messages you see."
##prompt += "\nWhat is your first name?"
##
##name = input(prompt)
##
##print("\nHello, " + name + "!")

def get_formated_name(first_name,last_name):
    """Возвращает аккуратно отформатированное полное имя"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Бесконечный цикл
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last nane: ")
    if l_name == 'q':
        break

    formatted_name = get_formated_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")