##cars = ['bmw','audi','toyota','subaru']
##cars.sort(reverse=True)
##print(cars)
##
##
##cars = ['bmw','audi','toyota','subaru']
##print("\nHere is The original list:")
##print(cars)
##
##print("\nHere is the sorted list:")
##print(sorted(cars))
##
##print("\nHere is the original list again:")
##print(cars)
##
### Вывод в обратном порядке
##
##print(cars)
##cars.reverse()
##print("\n")
##print(cars)
##print(len(cars))
##cars.reverse()
##
##for car in cars:
##    if car == 'bmw':
##        print(car.upper())
##    else:
##        print(car.title())

def make_car(manufacturer,model,**info_car):
    """Информация об автомобиле"""
    car = {}
    car['maker'] = manufacturer
    car['model'] = model
    for key, value in info_car.items():
        car[key] = value
    return car
car_info = make_car('subaru','outback',color='blue',tow_package=True)
print(car_info)
car_info = make_car('vaz','21099',color='red',forma='hatchback')
print(car_info)