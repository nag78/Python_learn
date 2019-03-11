def list_and(spisok):
    spisok[-1] = 'and ' + spisok[-1]
    return spisok

spisok = []
spisok = ['apples', 'bananas', 'tofu', 'cats']
print(list_and(spisok))
