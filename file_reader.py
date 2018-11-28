#-------------------------------------------------------------------------------
# Name:        file_reader
# Purpose:
#
# Author:      Nag
#
# Created:     28.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())