from collections import Counter

stuff = {'rope': 1, 'gold coin': 42}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + '  ' + k)
        item_total += v
    print ('Total number of items: ' + str(item_total))

def addToInventory(inventory, addItems):
    loot = Counter(addItems)
    for k in loot:
        if k in inventory:
            inventory[k] = inventory[k] + loot[k]
        else:
            inventory[k] = 1
    return inventory
c = addToInventory(stuff, dragonLoot)
displayInventory(c)


