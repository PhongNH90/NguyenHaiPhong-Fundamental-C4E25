pwd = input("Give your password please: ")
# print(pwd)

while len(pwd) <= 8 or pwd.isalpha() or pwd.isdigit() or not pwd.isalnum():
    print("Invalid, enter again")
    pwd = input("Give your password please: ")

print("You are OK")
