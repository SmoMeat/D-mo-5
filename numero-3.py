from turtle import forward as fd
from turtle import backward as bk
from turtle import right as rt
from turtle import left as lt
from turtle import penup as pu
from turtle import pendown as pd
# Voici la fonction polygoneReg qui permet de dessiner des polygones réguliers :
# def polygoneReg(cote, nbCotes):
#     for _ in range(nbCotes):
#         forward(cote)
#         right(360/nbCotes)
# Vous devez utiliser cette fonction, et possiblement définir d’autres fonctions, pour définir des fonctions
# qui dessinent les 6 figures géométriques suivantes :
# • triangle(cote) : un triangle équilatéral ayant des côtés de longueur cote
# • losange(cote) : un losange ayant des côtés de longueur cote et des angles de 60 et 120 degrés
# • hexagone(cote) : un hexagone formé de 6 triangles équilatéraux ayant des côtés de
# longueur cote
# • cube(cote) : un cube “3D” ayant des côtés de longueur cote
# • pyramide(cote,n) : une pyramide formée de n couches de triangles équilatéraux
# • bague(cote) : une bague formée de 6 triangles équilatéraux et 6 cubes qui s’alternent et qui
# ont des côtés de longueur cote
        

def draw_polygone(sides, side_lenght):
    for _ in range(sides):
        fd(side_lenght)
        rt(360/sides)
        
def draw_triangle(side_lenght):
    draw_polygone(3, side_lenght)

def draw_losange(side_lenght):
    for side in range(2):
        fd(side_lenght); rt(120)
        fd(side_lenght); rt(60)
    
def draw_hexagon(side_lenght):
    for side in range(6):
        draw_triangle(side_lenght)
        rt(60)
        
def draw_cube(side_lenght):
    for side in range(3):
        draw_losange(side_lenght)
        rt(120)

def draw_pyramide(side_lenght, layers):
    for layer in range(layers):
        for triangle in range(layer+1):
            draw_triangle(side_lenght)
            fd(side_lenght)
        pu()
        lt(90); fd(side_lenght); rt(90)
        bk(side_lenght*(layer+1.5))
        pd()
        
def draw_square(side_lenght):
    draw_polygone(4, side_lenght)
    
def draw_ring(side_lenght):
    for step in range(6):
        draw_triangle(side_lenght)
        fd(side_lenght); rt(30)
        draw_square(side_lenght)
        fd(side_lenght); rt(30)
        
lt(90)
#draw_losange(50)
#draw_triangle(80)
#draw_hexagon(80)
#draw_cube(80)
#draw_pyramide(16, 8)
draw_ring(20)