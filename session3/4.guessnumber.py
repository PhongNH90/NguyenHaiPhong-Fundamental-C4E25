from random import randint
x = randint(1,100)
print(x)

n = int(input("Random Number is: "))

while n != x:
    if n > x:
        print("Too high")
    elif n < x:
        print("Too low")
    n = int(input("Random Number is: "))

print("Bingo")

