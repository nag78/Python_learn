#-------------------------------------------------------------------------------
# Name:        display_message
# Purpose:
#
# Author:      Nag
#
# Created:     08.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def display_message(message):
    print (message)


message=input("Message: ")
display_message(message)

def favorite_book(book):
    print("Мне нравится " + book.title() +"!")
book = "Алиса в стране чудес"
favorite_book(book)