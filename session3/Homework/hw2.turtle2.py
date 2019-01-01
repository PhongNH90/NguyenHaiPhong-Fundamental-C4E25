from turtle import *
colors = ["red", "blue", "brown", "yellow", "grey"]

for i in colors:
    color(i)
    fillcolor(i)
    begin_fill()
    for i in range(2):
        fd(50)
        lt(90)
        fd(100)
        lt(90)
    fd(50)
    end_fill()

mainloop()