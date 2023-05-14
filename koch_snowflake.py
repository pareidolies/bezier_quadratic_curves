from tkinter import *
from turtle import *

def draw_line(n, L):
    if n==1:
        forward(L)
    else:
        draw_line(n - 1, L / 3.0)
        left(60)
        draw_line(n - 1, L / 3.0)
        right(120)
        draw_line(n - 1, L / 3.0)
        left(60)
        draw_line(n - 1, L / 3.0)

N = int(input("Number of levels (between 1 and 6) : "))
if (type(N) != int) or (N < 1) or (N > 6):
    print("Wrong number of levels")
else:
    Long = 550
    up()
    goto(-300, -180)
    down()
    width(2)
    left(60)
    for k in range(3):
        draw_line(N, Long)
        right(120)
    up()
    goto(0,0)
    mainloop()