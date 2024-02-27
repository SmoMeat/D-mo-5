from turtle import forward as fd
from turtle import backward as bk
from turtle import right as rt
from turtle import left as lt
from turtle import penup as pu
from turtle import pendown as pd
from turtle import *

def draw_black_box(size, x, y):
    pu(); goto(x-size/2, y); pd()
    pensize(size)
    fd(size)

def draw_echiquier(dimension):
    x = y = 0
    for col in range(dimension):
        for row in range(dimension):
            size = 10
            if col%2 == row%2:
                draw_black_box(size, col*size, row*size)
        
    
draw_echiquier(10)