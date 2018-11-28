#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nag
#
# Created:     28.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
else:
    #Подсчет приблизительного количества строк в файле.
    words  = contents.split()
    num_words = len(words)
    print('The file ' + filename + ' has about ' + str(num_words) +
        ' words.')