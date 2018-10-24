#-------------------------------------------------------------------------------
# Name:        aliens
# Purpose:
#
# Author:      Nag
#
# Created:     24.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

aliens = []
#Создание 30 зеленых пришельцев
for alien_number in range(30):
    new_alien = {
        'color':'green',
        'points':5,
        'speed':'slow'
        }
    aliens.append(new_alien)



#смена цветов пришельцев

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#Вывод первых 5 пришельцев

for alien in aliens[:5]:
    print(alien)
print("...")
print ("Total number of aliens: " + str(len(aliens)))