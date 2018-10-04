motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)


#motorcycles[0] = 'ducati'
# Добавление элемента списка в конец списка

motorcycles.append('ducati')
print(motorcycles)


motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)


del motorcycles[0]
print(motorcycles)



# Удаление с помощью pop()

poped_motorcycles = motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(0)
print("Последний мотокцил который уменя был это " + last_owned.title() + ".")


# Удаление элементов по значению

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me. ")

