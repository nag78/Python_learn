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
        self.login_attempts = 0

    def describe_user(self):
        print("\nUser: " + self.first_name.title() +
        " " + self.last_name.title())
        print("Group: " + self.group.title())
        print("Path: " + self.path_profile)
        print("Login Attempts: " + str(self.login_attempts))

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempst(self,attempts):

        if self.login_attempts > attempts:
            self.login_attempts = 0

new_user = User('nikolay','goltsev','administrators','/home/nag')
print(new_user.describe_user())
i=1
for i in range(1,7):
    new_user.increment_login_attempts()
    new_user.reset_login_attempst(5)
    new_user.describe_user()
    new_user.greet_user()
    i += i