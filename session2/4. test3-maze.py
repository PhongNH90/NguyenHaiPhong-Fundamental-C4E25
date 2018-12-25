from turtle import *
shape("turtle")
speed(100)

d = 100
for i in range(50):
    forward(d)
    left(90)
    d += 10 # d += -= *= /= == 10

mainloop()