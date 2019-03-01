# Игра в угадывагия чискел.
from random import randint


secretNumber = randint(1, 20)
print('Мной задумано число от 1 до 20. Попробуйте угадать.')

# Предоставить игроку 6 попыток.
for guessesTaken in range(1, 7):
    prompt = 'Ваш вариант: '
    guess = int(input(prompt))

    if guess < secretNumber:
        print('Ваше число меньше задуманного.')
    elif guess > secretNumber:
        print('Ваше число больше задуманного.')
    else:
        break # Правильное число
    

if guess == secretNumber:
    print('Верно! ' + str(secretNumber) + ' Попыток: ' + str(guessesTaken))
else:
    print('Нет! Задумано было: ' + str(secretNumber))