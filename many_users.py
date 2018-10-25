#-------------------------------------------------------------------------------
# Name:        many_users
# Purpose:
#
# Author:      Nag
#
# Created:     25.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

users = {
    'ainstein':{
        'first':'albert',
        'last':'einstein',
        'location':'priston'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',}
        }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
