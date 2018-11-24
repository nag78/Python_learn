#-------------------------------------------------------------------------------
# Name:        Car
# Purpose:
#
# Author:      Nag
#
# Created:     21.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
from car import Car

class Battery():
    """Простая модель аккумулятора автомобиля"""
    def __init__ (self, battery_size = 70):
        """Инициализирует аттрибуты аккумулятора"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("This car has a " + str(self.battery_size) + "kWh battery.")
    def get_range(self):
        """Выводит запас хода для аккумулятора"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """Представляет аспект машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя. Затем инициализируются
        специфичные для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()



