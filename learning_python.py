#-------------------------------------------------------------------------------
# Name:        learning_python
# Purpose:
#
# Author:      Nag
#
# Created:     28.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
filename = 'learning_python.txt'

##with open(filename) as file_object:
##    file = file_object.read()
##    print(file)

with open(filename) as file_object:
    for line in file_object:
        line = line.replace('Python','C')

        print(line.rstrip())

##strings = []
##with open(filename) as file_object:
##    lines = file_object.readlines()
##    for line in lines:
##        strings.append(line.strip())
##print(strings)