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

def print_file(filename):
    """Выводит на экран содержимое файла"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
##        print("The file " + filename + " does not exist.")
    else:
        print(contents.title())

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    print_file(filename)