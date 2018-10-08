guests = ['Andrey','Victor','Oleg']
print(guests[0].title() +" приходи на обед в пятницу!")
print(guests[1].title() +" приходи на обед в пятницу!")
print(guests[2].title() +" приходи на обед в пятницу!")

guests.remove('Oleg')
print(guests)
guests.append('Denis')

print(guests[0].title() +" приходи на обед в пятницу!")
print(guests[1].title() +" приходи на обед в пятницу!")
print(guests[2].title() +" приходи на обед в пятницу!")

guests.insert(0,'Polina')
guests.insert(1,'Nadya')
guests.append ('Oleg')

print(guests[0].title() +" приходи на обед в пятницу!")
print(guests[1].title() +" приходи на обед в пятницу!")
print(guests[2].title() +" приходи на обед в пятницу!")
print(guests[3].title() +" приходи на обед в пятницу!")
print(guests[4].title() +" приходи на обед в пятницу!")

print(guests)

print("\nВсего придет гостей:")
print(len(guests))

guests_lost =guests.pop()
print ('Извини ' + guests_lost + ' в пятницу не получится :(')
guests_lost=guests.pop()
print ('Извини ' + guests_lost + ' в пятницу не получится :(')
guests_lost=guests.pop()
print ('Извини ' + guests_lost + ' в пятницу не получится :(')
guests_lost=guests.pop()
print ('Извини ' + guests_lost + ' в пятницу не получится :(')

print(guests)

guest_last = guests[0]
print(guest_last.title() + " в пятницу все в силе!")
guest_last = guests[1]
print(guest_last.title() + " в пятницу все в силе!")

del guests[0]
del guests[0]

print(guests)
