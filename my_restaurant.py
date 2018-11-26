#-------------------------------------------------------------------------------
# Name:        my_restaurant
# Purpose:
#
# Author:      Nag
#
# Created:     26.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from restaurant import Restaurant

my_restaurant = Restaurant('vabi-sabi','asia')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(5)
print(my_restaurant.number_served)