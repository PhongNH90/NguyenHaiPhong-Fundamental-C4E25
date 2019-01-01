loop = True
while loop:
    n = input("Enter password ")
    loop = False # assume pass is ok
    if len(n) < 8:
        print("Pass must > 8")
        loop = True       
    if not n.isalnum():
        print("Pass must not contain special characters")
        loop = True
    if n.isdigit():
        print("Pass must contain letters")
        loop = True
    if n.isalpha():
        print("Pass must contain numbers")
        loop = True

print("Welcome")