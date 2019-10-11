def setup():
    size(300, 200)
    background(255, 255, 255)
    
    for x in range(0, 300):
        if x == 0:
            stroke(0, 0, 255)
        if x == 100:
            stroke(255, 255, 255)
        if x == 200:
            stroke(255, 0, 0)
        for y in range(0,200):
            point(x,y)

def draw():
    pass
