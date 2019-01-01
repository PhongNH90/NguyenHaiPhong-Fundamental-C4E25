print("Hi there, here you favorite things so far ")

items = ["Honda", "Toyota", "Hyundai"]
print(items)

x = input("Name one thing you want to add? ")
items.append(x)
print(items)

# y = input("Which one do you want to update? ")
z = int(input("Which one do you want to update? "))
items[z] = input("Change content: ")
print(items)

