def setup ():
    background(255)
    size(1000, 1000)
    espacement = 2 # espacement entreb  les lignes
    x1 = 0
    x2 = 1000 # init absis des lignes verticale
    for i in range(0, 1000, espacement):
        line(x1, 0, x2, 1000) # pour i = 0 ligne de haut-gauche à haut-droite 
        x1 = x1+espacement # basculemnt des lignes dans le sens des aiguille d'une montre
        x2 = x2-espacement
    y1 = 0
    y2 = 1000 # init absis des lignes horizontal
    for i in range(0, 1010, espacement):
        line(0, y1, 1000, y2) # idem basculement à l'horizontal
        y1 = y1+espacement
        y2 = y2-espacement
