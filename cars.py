cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)


cars = ['bmw','audi','toyota','subaru']
print("\nHere is The original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Вывод в обратном порядке

print(cars)
cars.reverse()
print("\n")
print(cars)
print(len(cars))
cars.reverse()

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
