#-------------------------------------------------------------------------------
# Name:        Car
# Purpose:
#
# Author:      Nag
#
# Created:     21.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Car():
    """Простая модель автомобиля"""
    def __init__(self,make,model,year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатировнное описание"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводиит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """Увеличивает показания одометра с заданным приращением"""
        self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора автомобиля"""
    def __init__ (self, battery_size = 70):
        """Инициализирует аттрибуты аккумулятора"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("This car has a " + str(self.battery_size) + "kWh battery.")

class ElectricCar(Car):
    """Представляет аспект машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя. Затем инициализируются
        специфичные для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()



my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()




my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()