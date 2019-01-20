
# #1. INPUT
x = int(input("x = "))
y = int(input("y = "))
pheptinh = input("pheptinh: ")


#2. process
result = 0

if pheptinh == "+":
    result = x + y

elif pheptinh == "-":
    result = x - y

elif pheptinh == "*":
    result = x * y

elif pheptinh == "/":
    result == x / y

#3. Output
print(result)


