#-------------------------------------------------------------------------------
# Name:        rollercoaster
# Purpose:
#
# Author:      Nag
#
# Created:     29.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
