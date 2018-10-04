motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)


#motorcycles[0] = 'ducati'

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




poped_motorcycles = motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

