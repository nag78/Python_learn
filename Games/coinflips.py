import random
print('Я подброшу монетку 1000 раз. Угадай, сколько раз выпадет "Орел"? (Нажмите клавишу Enter? чтобы начать)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1
    if flips == 900:
        print('900 подбрасываний и "Орел" выпал ' + str(heads) + ' раз.')
    if flips == 100:
        print('100 подбрасываний и "Орел" выпал ' + str(heads) + ' раз.')
    if flips == 500:
        print('500 подбрасываний и "Орел" выпал ' + str(heads) + ' раз.')
print()
print('Из  1000 подбрасываний "Орел" выпал ' + str(heads) + ' раз.')
print('Насколько близки вы были к правильному ответу?')