from tkinter import *
from turtle import *

def draw_segment(x1, y1, x2, y2):
    up()
    goto(x1, y1)
    down()
    goto(x2, y2)
    up()

def middle(x1, y1, x2, y2):
    return (x1 + x2) / 2., (y1 + y2) / 2.

def bezier(xa, ya, xb, yb, xc, yc, n):
    if n == 0:
        draw_segment(xa, ya, xb, yb)
        draw_segment(xb, yb, xc, yc)
    else:
        xd, yd = middle(xa, ya, xb, yb)
        xe, ye = middle(xb, yb, xc, yc)
        xf, yf = middle(xd, yd, xe, ye)
        bezier(xa, ya, xd, yd, xf, yf, n-1)
        bezier(xf, yf, xe, ye, xc, yc, n-1)

bezier(40, 80, 0, 10, 60, 30, 3)
bezier(30, 0, 40, 30, 50, 60, 3)
bezier(70, 60, 100, 80, 80, 40, 3)
bezier(80, 40, 70, 20, 100, 30, 3)
mainloop()