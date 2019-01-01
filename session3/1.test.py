n = input("Your year of birth? ")

while not n.isdigit():
    print("You must enter in number, please enter again!")
    n = input("Your year of birth? ")

yob = int(n)
age = 2018 - yob
print(age)
