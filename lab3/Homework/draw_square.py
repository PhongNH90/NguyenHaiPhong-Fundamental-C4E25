from turtle import *

def draw(length,color):
    for i in range(4):
        pencolor(color)
        fd(length)
        lt(90)
        
draw(100,"red")

for i in range(30):
    draw(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()


mainloop()