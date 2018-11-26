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

    def set_number_served(self,served):
        self.number_served = served

    def increment_number_served(self,served):
        self.number_served += served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name,cuisine_type)
        self.flavours = ['vanila','strawberry','banan','chokolad']
    def iceflavour(self):
        print("\nIce flavours: ")
        for flavour in self.flavours:
            print(flavour)
