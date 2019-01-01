items = ["T-shirt", "Sweater"]
x = "Welcome to our shop, what do you want?"
print(x)
print("Our items: ", items)

# y = input("Enter your items: ")
# items.append(y)
# print("Our items: ", items)


z = int(input("Update postion? "))
a = input("New item: ")
items[z] = a
print("Our items: ", items)

re = int(input("Delete position: "))
items.pop(re)
print("Our items: ", items)
