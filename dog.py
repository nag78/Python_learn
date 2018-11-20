#-------------------------------------------------------------------------------
# Name:        Dog
# Purpose:
#
# Author:      Nag
#
# Created:     20.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Dog():
    """Простая модель собаки"""

    def __init__(self, name,age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """ Собака переворачивается по команде."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie',6)
print("My dog's name is " + my_dog.name.title() +".")
print("My dog is " + str(my_dog.age) + " years old.")
