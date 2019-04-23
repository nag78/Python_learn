# Программа читает содержимое текстового файла infile.txt
# Находит в вхождение слов ADJECTIVE(прилагательное),
# NOUN(существительное), ADVERB(наречие) и VERB(глагол)
# и предоставляет возможность пользователю заменить их
# результат выводится на экрран и в файл outfile.txt


infile = open('d:\\Python\\Python_learn\\Al Sweigart\\MadLibs\\infile.txt',
              'r')
outfile = open('d:\\Python\\Python_learn\\Al Sweigart\\MadLibs\\outfile.txt',
               'w')
inStr = infile.read()


def findWord(inS, word):
    # Найти и заменить слова в строке.
    outS = ''

    if word == 'NOUN':
        prompt = 'Введите существительное. '
        newWord = input(prompt)
        outS = inS.replace(word, newWord, 1)
    elif word == 'ADJECTIVE':
        prompt = 'Введите прилагательное. '
        newWord = input(prompt)
        outS = inS.replace(word, newWord, 1)
    elif word == 'VERB':
        prompt = 'Введите глагол. '
        newWord = input(prompt)
        outS = inS.replace(word, newWord, 1)
    elif word == 'ADVERB':
        prompt = 'Введите наречие. '
        newWord = input(prompt)
        outS = inS.replace(word, newWord, 1)
    return outS


words = ['NOUN', 'ADJECTIVE', 'VERB', 'ADVERB', ]
outStr = inStr
for word in words:
    i = 1
    max = outStr.count(word)
    for i in range(max):
        outStr = findWord(outStr, word)

outfile.write(outStr)
print(outStr)
infile.close()
outfile.close()
