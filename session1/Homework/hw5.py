from turtle import *
shape("turtle")
speed(100)

fillcolor("blue")
begin_fill()
for i in range(100):
    circle(100)
    left(7)
end_fill()
mainloop()