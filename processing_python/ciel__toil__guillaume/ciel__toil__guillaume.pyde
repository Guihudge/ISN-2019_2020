from random import randint 

def setup():
    size(800, 600)
    background(0, 0, 0)

def draw():
    stroke(255, 255, 255)
    x = randint(0, 800)
    y = randint(0, 600)
    point(x, y)
    
