n = int(input("n = "))
for i in range(1,n+1):
    if i % 2 == 0:
        print("*", end="")
    
    elif i % 2 == 1:
        print("x", end="")

