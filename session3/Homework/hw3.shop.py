x = input("Welcome to our shop, what do you want? (C, R, U, D) ")
print(x)

items = ["T-shirt", "Sweater"]

while True:
    if x == "R":
        print("Our items: ", items)
        x = input("Welcome to our shop, what do you want? (C, R, U, D) ")

    elif x == "C":
        y = input("Enter your items: ")
        items.append(y)
        print("Our items: ", items)
        x = input("Welcome to our shop, what do you want? (C, R, U, D) ")

    elif x == "U":
        z = int(input("Update postion? "))
        a = input("New item: ")
        items[z] = a
        print("Our items: ", items)
        x = input("Welcome to our shop, what do you want? (C, R, U, D) ")

    elif x == "D":
        re = int(input("Delete position: "))
        items.pop(re)
        print("Our items: ", items)
        x = input("Welcome to our shop, what do you want? (C, R, U, D) ")

