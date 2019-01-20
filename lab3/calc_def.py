# def #day la mot function "ham"

# def sayHi():        #tên hàm là sayHi       #khai báo Hàm
#     print("Hi", "Phong")     #thân hàm (function body)
#     print("Bye")
# sayHi()
# sayHi()


# def sayHi(n):        #tên hàm là sayHi       #khai báo Hàm
#     print("Hi", n)     #thân hàm (function body)
#     print("Bye")
# sayHi("Phong")
# sayHi("Tuan")


# def add(x, y):
#     r = x + y
#     print(r)
# add(3,4)


# def add(x, y):
#     r = x + y
#     return r        #đưa r ra khỏi box  #hàm có trả về kết quả, sử dụng cho phép tính sau

# s = add(3,4)        #hứng r vào s
# print(s)

# t = add(6,7)
# print(t)


def eval(x,y,pheptinh):
    result = 0

    if pheptinh == "+":
        result = x + y

    elif pheptinh == "-":
        result = x - y

    elif pheptinh == "*":
        result = x * y

    elif pheptinh == "/":
        result == x / y

    return result

# r = eval(4,5,"*")         
# print(r)

x = int(input("x = "))
y = int(input("y = "))
pheptinh = input("pheptinh: ")

r = eval(x,y,pheptinh)
print(r)