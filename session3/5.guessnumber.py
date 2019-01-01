from random import randint
x = randint(1,100)
print(x)

n = int(input("Random Number is: "))
loop = True
while loop:
    if n == x:
        print("Bingo")




        
    elif n < x:
        print("Too low")
    n = int(input("Random Number is: "))

print("Bingo")