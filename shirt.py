#-------------------------------------------------------------------------------
# Name:        shirt
# Purpose:
#
# Author:      Nag
#
# Created:     12.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def make_shirt(size='L',text='I love Python'):
    """Размер и текст футболки"""
    print("\nMy shirt " + size + ", My print is '" + text.title() + "!'")
make_shirt()
make_shirt(text='I am not love Brainfuck')