from random import randint, choice
# import calc_def         #đây là cách import rất phổ biến, import trực tiếp tên file ()
from calc_def import eval      #phổ biến, dễ dùng hơn


x = randint(0,9)
y = randint(0,9)
op = choice(["+","-","*","/"])
error = randint(-1,1)
# r = x + y + error
# r = calc_def.eval(x,y,op) + error           #lấy dữ liệu đã có ở 1 file cùng trong lab3 
r = eval(x,y,op) + error

print(x, op, y, "=", r)

user_input = input("Your answer (Y/N) ").upper()

result = ""   #best practice
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