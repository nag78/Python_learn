#-------------------------------------------------------------------------------
# Name:        magicans
# Purpose:
#
# Author:      Nag
#
# Created:     17.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def show_magicans(magicans):
##    print(magicans)
    for magic in magicans:
        print(magic)

def make_great(magicans, great_magicans):
    while magicans:
        curr_magic = magicans.pop()
        great_magic = 'Great ' + curr_magic.title() + '!'
        great_magicans.append(great_magic)

great_magicans = []
magicans = ['kio','popov']
make_great(magicans[:],great_magicans)
show_magicans(great_magicans)
show_magicans(magicans)