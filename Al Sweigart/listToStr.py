def listToStr(list):
    string = ''
    for i in range(len(list) - 1):
        string = string + list[i] + ', '

    string = string + 'and ' + list[-1]
    return string


spam = ['apples', 'bananas', 'tofu', 'cats', 'python']
print(listToStr(spam))
