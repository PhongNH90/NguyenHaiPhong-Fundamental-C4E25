yob_str = input("Nam sinh? ")

while not yob_str.isdigit():
    print("Not a number, Enter again ")
    yob_str = input("Nam sinh? ")
    
yob = int(yob_str)
age = 2018 - yob
print(age)