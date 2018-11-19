##pizzas = ['papa johns','margarita','pepperoni']
##
##friend_pizzas = pizzas[:]
##pizzas.append('mexican')
##friend_pizzas.append('gavai')
##
##print("My favorite pizzas are:")
##print(pizzas)
##
##print("My friend's favorite pizzas are:")
##print(friend_pizzas)
##
##
##for pizza in pizzas:
##    print("I like a " + pizza.title() + "!\n")
##print ("I really love pizza!")
##
##for pizza in friend_pizzas:
##    print("I like a " + pizza.title() + "!\n")
##print ("I really love pizza!")
##
###Сохранение информации о заказанной пицце
##
##pizza = {
##    'crust':'thick',
##    'toppings':['mushrooms','extra cheese'],
##    }
##
###Описание заказа.
##
##print("You ordered a " + pizza['crust'] + "-crustpizza " +
##    "with the following toppings:")
##for topping in pizza['toppings']:
##    print("\t" + topping)

##prompt = "\nEnter you want toping."
##prompt += "\n(Enter 'quit' for exit!"

##while True:
##    topings = input(prompt)
##    if topings == 'quit':
##        break
##    else:
##        print("Plese add me in pizza " + topings.title() + "!")

##active = True
##while active:
##    topings = input(prompt)
##    if topings == 'quit':
##        active = False
##    else:
##        print("Plese add me in pizza " + topings.title() + "!")
##topings = ''
##while topings != 'quit':
##    topings = input(prompt)
##    if topings != 'quit':
##        print("Plese add me in pizza " + topings.title() + "!")

def make_pizza(size,*toppings):
    """Вывод описания пиццы"""
    print("\nMaking a " + str(size) +
            "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')





