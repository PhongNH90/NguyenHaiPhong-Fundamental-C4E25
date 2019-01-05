result = [35,36,40,44]

print("If x = 8, then what is the value of 4(x+3)? ")
for index, i in enumerate(result):
    print(index+1, i, sep=". ")

ques = int(input("Your answer: "))

loop = True
while loop:
    if ques == 4:
        print("Bingo")
        loop = False
    else:
        print("Pleasy try again")
        ques = int(input("If x = 8, then what is the value of 4(x+3)? "))