# Программа читает содержимое текстового файла infile.txt
# Находит в вхождение слов ADJECTIVE(прилагательное),
# NOUN(существительное), ADVERB(наречие) и VERB(глагол)
# и предоставляет возможность пользователю заменить их
# результат выводится на экрран и в файл outfile.txt


infile = open('infile.txt', 'r')
inStr = infile.read()


def findWord(inS, word):
    # Найти и заменить слова в строке.
    newWord = input()
    outS = inS.replace(word, newWord, 1)
    return outS


