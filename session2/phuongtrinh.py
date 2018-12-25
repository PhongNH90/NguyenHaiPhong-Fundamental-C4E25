a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b**2 - 4*a*c
a_2 = 2*a
if delta < 0:
    print("Vo nghiem")

elif delta == 0:
    x = -b // a_2
    print("Nghiem phuong trinh la ", x)

else:
    delta_sqrt = delta**0.5
    x1 = (-b + delta_sqrt)//a_2
    x2 = (-b - delta_sqrt)//a_2
    print("Nghiem 1, x1=", x1, "Nghiem 2, x2=", x2)



