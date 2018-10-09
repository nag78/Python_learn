#-------------------------------------------------------------------------------
# Name:        20
# Purpose:
#
# Author:      Nag
#
# Created:     09.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

numbers = []
for number in range(1,21):
    numbers.append(number)
    print(number)

numbers = [number for number in range(19,0,-2)]
numbers.reverse
print(numbers)
