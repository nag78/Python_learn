#-------------------------------------------------------------------------------
# Name:        counting
# Purpose:
#
# Author:      Nag
#
# Created:     30.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


##current_number = 1
##while current_number <= 5:
##    print(current_number)
##    current_number += 1

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)