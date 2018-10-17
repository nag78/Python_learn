#-------------------------------------------------------------------------------
# Name:        amusement_park
# Purpose:
#
# Author:      Nag
#
# Created:     17.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

age = 12

if age < 4:
    price = 0
#   print ("Your admission cost is $0.")
elif age < 18:
    price = 5
#   print ("Your admission cost is $5.")
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
#    print ("Your admission cost is $10.")


print ("Your admission cost is $" + str(price) + ".")