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

        for line in f_obj:
            line = line.lower()
            count = line.count(word)
            print(line.strip())
            count += count
        print(str(count))

line_count('alice.txt'," project ")
