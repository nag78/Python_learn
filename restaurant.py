#-------------------------------------------------------------------------------
# Name:        restaurant
# Purpose:
#
# Author:      Nag
#
# Created:     20.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant have name " + "'" + self.restaurant_name.title()
         + "'" + "!")
        print("Cuisine: " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant " + "'" + self.restaurant_name.title()
         + " is Open!")

japan_rest = Restaurant('vabi-sabi','asian')
japan_rest.describe_restaurant()


ital_rest = Restaurant('el patio', 'italian')
ital_rest.describe_restaurant()

ua_rest = Restaurant('kumanek','ukranian')
ua_rest.describe_restaurant()

