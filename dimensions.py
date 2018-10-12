#-------------------------------------------------------------------------------
# Name:        dimensions
# Purpose:
#
# Author:      Nag
#
# Created:     12.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


dimensions = (200,50)
## print(dimensions[0])
## print(dimensions[1])

# print(dimensions)

print("Original dimesnions:")
for dimension in dimensions:
    print(dimension)

print("Modified dimensions:")
dimensions = (400,100)
for dimension in dimensions:
    print(dimension)