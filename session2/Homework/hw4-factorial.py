n = int(input("n = "))
factorial = 1

if n < 0:
    print("Sorry,factorial does not exist for negative number")

elif n == 0:
    print("The factorial of 0 is 1")

else:
    for i in range(1, n+1):
        factorial *= i

print("The factorial of",n, "=", factorial)