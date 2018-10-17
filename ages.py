#-------------------------------------------------------------------------------
# Name:        ages
# Purpose:
#
# Author:      Nag
#
# Created:     17.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


age =132

if age < 2:
    man = 'младенец'
elif age < 4:
    man = 'малыш'
elif age < 13:
    man = 'ребенок'
elif age < 20:
    man = 'подросток'
elif age < 65:
    man = 'взрослый'
elif age >= 65:
    man = 'пожилой человек'

print (man)