#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nag
#
# Created:     27.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint

class Die():
    """Модель кубика"""
    def __init__ (self,sides = 6):
        """Инициализируем стороны"""
        self.sides = sides

    def roll_die(self):
        """Бросок кубика"""
        sides = randint(1,self.sides)
        print("Sides: " + str(sides))

shoot = Die(20)
i=0
for i in range(0,10):
    shoot.roll_die()
    i += i
