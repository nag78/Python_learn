#-------------------------------------------------------------------------------
# Name:        favorite_numbers
# Purpose:
#
# Author:      Nag
#
# Created:     23.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

favorite_numbers = {
    'ivan' : 5,
    'nikolay' : 11,
    'marina' : 6,
    'svetlana' : 21,
    'denis' : 22
    }
##print("Любимое число Николая:\n")
##print( str(favorite_numbers['nikolay']))


for key , value in favorite_numbers.items():
    print("\nKey", key)
    print("Value", str(value))