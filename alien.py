#-------------------------------------------------------------------------------
# Name:        alien
# Purpose:
#
# Author:      Nag
#
# Created:     22.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Работа со словарями

alien_0 = {'color':'green','points':5}

##print(alien_0['color'])
##print(alien_0['points'])

#new_points = alien_0['points']
#print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print ("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print ("The alien is now " + alien_0['color'] + ".")