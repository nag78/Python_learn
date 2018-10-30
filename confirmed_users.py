#-------------------------------------------------------------------------------
# Name:         confirmed_users
# Purpose:
#
# Author:      Nag
#
# Created:     30.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Два списка: неповереного и пустого для хранения значений


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#Проверяем пока в списке есть не проверенные


while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifyng user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())