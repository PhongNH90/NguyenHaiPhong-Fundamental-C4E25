from random import randint

correct = 0
while True:
    x = randint(0,9)
    y = randint(0,9)
    error = randint(-1,1)
    r = x + y + error

    print(x, "+", y, "=", r)

    user_input = input("Your answer (Y/N) ")

    result = ""
    
    if error == 0:
        if user_input == "Y":
            result = "Yay"
            correct += 1
        else:
            result = "Wrong"
    else:
        if user_input == "Y":
            result = "Wrong"
        else:
            result = "Yay"
            correct += 1

    print(result)
    print("Count correct number = ",correct)