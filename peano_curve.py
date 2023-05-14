from tkinter import *
from turtle import *

def hilbert(depth, length, angle):
    if depth == 0:
        return
    right(angle)
    hilbert(depth - 1, length, -angle)
    forward(length)
    left(angle)
    hilbert(depth - 1, length, angle)
    forward(length)
    hilbert(depth - 1, length, angle)
    left(angle)
    forward(length)
    hilbert(depth - 1, length, -angle)
    right(angle)
    
size = 400
penup()
goto(-size/4, size/4)
pendown()

hilbert(4, size/(24 - 1), 90)

mainloop()