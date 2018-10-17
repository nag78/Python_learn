#-------------------------------------------------------------------------------
# Name:        banned_users
# Purpose:
#
# Author:      Nag
#
# Created:     17.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")