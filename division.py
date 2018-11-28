#-------------------------------------------------------------------------------
# Name:        division
# Purpose:
#
# Author:      Nag
#
# Created:     28.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")