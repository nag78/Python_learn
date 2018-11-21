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

##def get_formated_name(first_name,last_name):
##    """Возвращает аккуратно отформатированное полное имя"""
##    full_name = first_name + ' ' + last_name
##    return full_name.title()
##
### Бесконечный цикл
##while True:
##    print("\nPlease tell me your name:")
##    print("(enter 'q' at any time to quit)")
##
##    f_name = input("First name: ")
##    if f_name == 'q':
##        break
##
##    l_name = input("Last nane: ")
##    if l_name == 'q':
##        break
##
##    formatted_name = get_formated_name(f_name,l_name)
##    print("\nHello, " + formatted_name + "!")

class User():
    def __init__(self,first_name,last_name,group,path_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.path_profile = path_profile

    def describe_user(self):
        print("\nUser: " + self.first_name.title() +
            " " + self.last_name.title())
        print("Group: " + self.group.title())
        print("Path: " + self.path_profile)

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " +
            self.last_name.title() + "!")

new_user = User('nikolay','goltsev','administrators','/home/nag')
print(new_user.describe_user())
print(new_user.greet_user())