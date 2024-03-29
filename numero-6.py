from turtle import forward as fd
from turtle import backward as bk
from turtle import right as rt
from turtle import left as lt
from turtle import penup as pu
from turtle import pendown as pd
from turtle import *

def draw_moulin():
    pd()
    pensize(50)
    pencolor(0.3, 0.3, 0.3)
    lt(90)
    fd(100)
    pu()
    
def draw_ailes(num):
    pass

def draw_one_wing(length):
    pd()
    fd(length)
    rt(90)
    fd(length/2)
    rt(115)
    fd(length)
    
    pu()
    fd(20)
    
lt(90)
draw_one_wing(50)
draw_moulin()

mainloop()
