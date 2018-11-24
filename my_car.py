#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nag
#
# Created:     24.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from car import Car
from electric_car import ElectricCar

my_beetly = Car('volkswagen','beetly',2016)
print(my_beetly.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())