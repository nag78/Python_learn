#-------------------------------------------------------------------------------
# Name:        user_profile
# Purpose:
#
# Author:      Nag
#
# Created:     19.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def build_profile(first,last,**user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('nikola', 'goltsev',
                                city = 'moscow',
                                field = 'it')
print(user_profile)
