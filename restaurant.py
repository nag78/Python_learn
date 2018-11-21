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
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant have name " + "'" + self.restaurant_name.title()
         + "'" + "!")
        print("Cuisine: " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant " + "'" + self.restaurant_name.title()
         + " is Open!")

japan_rest = Restaurant('vabi-sabi','asian')
japan_rest.describe_restaurant()
print(str(japan_rest.number_served))
japan_rest.number_served = 15
print(str(japan_rest.number_served))

ital_rest = Restaurant('el patio', 'italian')
ital_rest.describe_restaurant()

ua_rest = Restaurant('kumanek','ukranian')
ua_rest.describe_restaurant()

restaurant = Restaurant('2x2','european')
restaurant.describe_restaurant()
restaurant.number_served = 4
print("Served: " + str(restaurant.number_served))