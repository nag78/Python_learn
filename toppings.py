#-------------------------------------------------------------------------------
# Name:        toppings
# Purpose:
#
# Author:      Nag
#
# Created:     17.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-----------------------------------------------------------------------
requested_toppings =['mushrooms','onion','pineapple','extra_cheese']
#'mushrooms' in requested_topping

if 'mushrooms' in requested_toppings:
#     print("Hold the mushrooms!")
    print("Adding mushrooms.")
if 'peperoni' in requested_toppings:
    print("Adding peperoni")
if 'extra_cheese' in requested_toppings:
    print("Adding extra_cheese")


print("\nFinished making your pizza!")


requested_toppings = ['mushrooms','green pepper','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("Sorry, we are out of green peppers rigth now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinisher making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza!")

