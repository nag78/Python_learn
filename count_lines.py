#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nag
#
# Created:     29.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def line_count(filename,word):
    global counter
    with open(filename) as f_obj:

        for line in f_obj:

            line = str(line.lower().split())

            counter += line.count(word)
        print(counter)

file = input("Input filename: ")
word = input("Input word: ")

counter = 0
line_count(file,word)
