#-------------------------------------------------------------------------------
# Name:        montains_poll
# Purpose:
#
# Author:      Nag
#
# Created:     30.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

responses = {}

polling_active = True
while polling_active:
    name = input("\nWhats is your name? ")
    response = input("Which mountain whould you like to climb someday? ")

    responses[name] = response
    repeat = input("Would you like to let another person rspond? (yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n --- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")

