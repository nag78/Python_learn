#-------------------------------------------------------------------------------
# Name:        greet_users
# Purpose:
#
# Author:      Nag
#
# Created:     02.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def greet_user(names):
    """Выводит простое приветствие для каждого пользователя в списке"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)


##    print ("Hello, " + username.title() + "!")
##greet_user('jesse')
##
##greet_user('sarah')
##
