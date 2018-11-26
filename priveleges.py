#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nag
#
# Created:     26.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from usernew import User

class Priveleges():
    def __init__(self,priveleges = []):
        self.priveleges = priveleges

    def show_priveleges(self):

        print(self.priveleges)


class Admin(User):
    def __init__(self,first_name,last_name,group,path_profile):
        super().__init__(first_name,last_name,group,path_profile)
        priveleges = ['R/W messages','add/del users','ban users']
        self.priveleges = Priveleges(priveleges)


