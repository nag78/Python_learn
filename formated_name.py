#-------------------------------------------------------------------------------
# Name:        formated_name
# Purpose:
#
# Author:      Nag
#
# Created:     14.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_formated_name(first_name,last_name,middle_name =''):
    """Возвращает аккуратно отформатированное полное имя"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' '  + last_name
    return full_name.title()

musician = get_formated_name('jimi','hendrix')
print(musician)

musician = get_formated_name('john','hooker','lee')
print(musician)