#-------------------------------------------------------------------------------
# Name:        rivers
# Purpose:
#
# Author:      Nag
#
# Created:     23.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
rivers = {
    'Нил' : 'Египет',
    'Волга' : 'Россия',
    'Хуанхэ' : 'Китай'
    }
for river, state in rivers.items():
    print ("Река " + river + " протекает в " + state + ".")

for river in rivers.keys():
    print(river)

for state in rivers.values():
    print(state)