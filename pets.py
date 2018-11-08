#-------------------------------------------------------------------------------
# Name:        pets
# Purpose:
#
# Author:      Nag
#
# Created:     30.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
##print(pets)
##
##while 'cat' in pets:
##    pets.remove('cat')
##print(pets)

def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet('dog', 'willie')