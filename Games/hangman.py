import random
HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
    |
     |
     |
    ===''', '''
 +---+
 o   |
 |   |
     |
    ===''', '''
 +---+
 o   |
/|   |
     |
    ===''', '''
 +---+
 o   |
/|\  |
     |
    ===''', '''
 +---+
 o   |
/|\  |
/    |
    ===''', '''
 +---+
 o   |
/|\  |
/ \  |
    ===''']

words = 'аист акула бабуин баран барсук бобр бык верблюд волк ворбей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()

def getRandomWord(wordList):
    # Эта функция возвращает случайную строку из переданного списка.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Заменяет пропуск отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше.
    while True:
        print('Введите букву.')
        guess = input()
        guess.lower()
        if len(guess) != 1:
            print('Пожалуйста введите только одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста введиту БУКВУ.')
        else:
            return guess

def playAgain():
    # Функция возвращает True, если игрок хочет сыграть зано.
    print('Хотите сыграть ещё? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False


while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Позволяет игроку ввести букву.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # проверяем выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверяем превысил ли игрок лимит попыток и роиграл.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали попытки! \nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано ' + str(len(correctLetters)) + ' было загадано ' + secretWord)
            gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
