#-------------------------------------------------------------------------------
# Name:        favorite_laguages
# Purpose:
#
# Author:      Nag
#
# Created:     22.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
##print("Sarah's favorite language is " +
##    favorite_languages['sarah'].title() +
##    ".\n")


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+
        language.title() + ".")

print("\n")


##for name in favorite_languages.keys():
##    print(name.title())

friends = ['phil','sarah']
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())



pools = ['nikolay','sarah','svetlana','phil','marina','ilya']
for name in pools:
    if name in favorite_languages:
        print(name.title() + ", спасибо за участие в опросе!")
    else:
        print(name.title() + ", пожалуйста примите участие в опросе!")