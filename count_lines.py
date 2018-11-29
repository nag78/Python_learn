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

    with open(filename) as f_obj:
        lines = f_obj.readlines()
        for line in lines:
            count = line.strip().lower().count(word)
            count += count
    print(str(count))

line_count('legends.txt','of')
