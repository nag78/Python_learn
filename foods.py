#-------------------------------------------------------------------------------
# Name:        foods
# Purpose:
#
# Author:      Nag
#
# Created:     09.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
my_foods = ['pizza','falafel','carrot_cake']
frien_foods = my_foods [:]

my_foods.append('cannoli')
frien_foods.append('ice_cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(frien_foods)

print("The first three items in the list are:")
print(my_foods[:3])
print("The middle three items in the list are:")
print(my_foods[1:-1])
print("The last three items in the list are:")
print(my_foods[1:])