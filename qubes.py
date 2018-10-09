#-------------------------------------------------------------------------------
# Name:        qubes
# Purpose:
#
# Author:      Nag
#
# Created:     09.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

qubes = [value **3 for value in range(1,11)]
print(qubes)


qubes = []
for value in range(1,11):
    qubes.append(value **3)
    print(qubes)