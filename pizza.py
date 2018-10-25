pizzas = ['papa johns','margarita','pepperoni']

friend_pizzas = pizzas[:]
pizzas.append('mexican')
friend_pizzas.append('gavai')

print("My favorite pizzas are:")
print(pizzas)

print("My friend's favorite pizzas are:")
print(friend_pizzas)


for pizza in pizzas:
    print("I like a " + pizza.title() + "!\n")
print ("I really love pizza!")

for pizza in friend_pizzas:
    print("I like a " + pizza.title() + "!\n")
print ("I really love pizza!")

#Сохранение информации о заказанной пицце

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }

#Описание заказа.

print("You ordered a " + pizza['crust'] + "-crustpizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)