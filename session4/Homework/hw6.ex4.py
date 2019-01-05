print("QUESTION 1")
result_1 = [35,36,40,44]

print("If x = 8, then what is the value of 4(x+3)? ")
for index, i in enumerate(result_1):
    print(index+1, i, sep=". ")

ques = int(input("Your answer: "))

correct = 0
if ques == 4:
    print("Bingo! Please next to question 2 ")
    correct += 1

else:
    print(":( You need to be more focusing. Please next to question 2 ")

        
print()

print("QUESTION 2")
result_2 = ["About 55", "About 65", "About 75", "About 85"]

print("Jack scored these marks: 49,81,72,55 and 62. What does it mean? ")
for index_2, j in enumerate(result_2):
    print(index_2+1, j, sep=". ")

ques = int(input("Your answer: "))


if ques == 2:
    print("Bingo")
    correct += 1

else:
    print(":(" )

print("Overall, the number of your correct answer is: ", correct)
