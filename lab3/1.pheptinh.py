from random import randint

#1. input

x = randint(0,9)
y = randint(0,9)
error = randint(-1,1)
r = x + y + error

print(x, "+", y, "=", r)

user_input = input("Your answer (Y/N) ").upper()


result = ""   #best practice        #nên làm cách này thay vì print từng kết quả phía dưới
if error == 0:
    if user_input == "Y":
        result = "Yay"
    else:
        result = "Wrong"
else:
    if user_input == "Y":
        result = "Wrong"
    else:
        result = "Yay"

print(result)


#về nhà đếm câu hỏi đúng
#làm giống bài tập về nhà

