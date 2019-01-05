inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ["seashell", "strangeberry", "lint"]
# print(inventory)

inventory["backpack"].pop(1)   

# inventory["backpack"].remove("dagger")
# print(inventory["backpack"])

inventory["gold"] += 50
print(inventory)
