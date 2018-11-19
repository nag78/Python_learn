#-------------------------------------------------------------------------------
# Name:        sandwich
# Purpose:
#
# Author:      Nag
#
# Created:     19.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def make_sandwich(*toppings):
    """Make a sandwich"""
    print("\nMaking a sandwich." )
    print("Toppings: ")
    for topping in toppings:
        print("- " + topping)
make_sandwich('backon','cheese')
make_sandwich('sausage','cheese','ketchup')
make_sandwich('souse','chiken grill', 'exta cheese', 'grill backon')