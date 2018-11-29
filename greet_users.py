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
import json

def greet_user(names):
    """Выводит простое приветствие для каждого пользователя в списке"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

filename = 'username.json'
with open(filename) as f_obj:
    username = str(json.load(f_obj))
print(username)