#-------------------------------------------------------------------------------
# Name:        printing models
# Purpose:
#
# Author:      Nag
#
# Created:     16.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Список моделей который необходимо напечатать

unprinted_disign = ['iphone case','robot pendant','dodecahedron']
completed_models = []

## Цикл последовательно печатает каждую модель из списка.
## После печачти модель перемещается в другой список

while unprinted_disign:
    current_disign = unprinted_disign.pop()
    ##  Печать 3Д модели
    print("Printing model: " + current_disign)
    completed_models.append(current_disign)

# Вывод всех готовых моделей
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)