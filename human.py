#-------------------------------------------------------------------------------
# Name:        human
# Purpose:
#
# Author:      Nag
#
# Created:     23.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

human = {
    'first_name' : 'nikolay',
    'last_name' : 'goltsev',
    'age' : '40',
    'city' : 'moscow'
    }

woman = {
    'first_name' : 'svetlana',
    'last_name' : 'goltseva',
    'age' : '34',
    'city' : 'moscow'
    }

mother = {
    'first_name' : 'tamara',
    'last_name' : 'goltseva',
    'age' : '80',
    'city' : 'shadrinsk'
    }

people = [human,woman,mother]

##print(people)


for man in people:
##    print(man)
    for key in man.keys():
        full_info = man[key].title()
        print(full_info)
