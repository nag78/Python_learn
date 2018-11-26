#-------------------------------------------------------------------------------
# Name:        new_user
# Purpose:
#
# Author:      Nag
#
# Created:     26.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from priveleges import *


my_admin = Admin('nikolay','goltsev','admins','/home/nag')
my_admin.describe_user()
my_admin.priveleges.show_priveleges()

# my_user = User('user', ' ','users','/home/user')
# my_user.describe_user()
# my_user.priveleges.show_priveleges()
