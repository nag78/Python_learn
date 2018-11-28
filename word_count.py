#-------------------------------------------------------------------------------
# Name:        word_count
# Purpose:
#
# Author:      Nag
#
# Created:     28.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        #Подсчет приблизительного количества строк в файле
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
            " words.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)