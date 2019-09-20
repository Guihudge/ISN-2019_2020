def somme2 (n):
    x = 0
    for i in range(0, n):
        x = x + (i**3) # met la valeur x au cube et l'ajoute à lui meme
    print(x)

def fact(n):
    # somme(3) = 1+2+3
    l = []
    x=1
    for i in range(1, n+1):
        l.append(i)
    # print(l)
    
    for i in l:
        x = x*i
        print(x)

def diviseur(n):
    diviseur = []
    for i in range(1,n+1): # teste tous les diviseurs de 1 à 100
        test = n%i # teste la divisibilité
        if test == 0:
            diviseur.append(i) # ajoute le diviseur à la liste des diviseurs
    return diviseur

def syracuse(n):
    rep = []
    run = True
    while run:
        rep.append(n) # ajout de la réponse à la liste

        test = n%2 # test paire
        if n == 1:
            run = False
        elif test == 1:
            n = (3*n)+1
        elif test == 0:
            n = n/2
        
    return rep

def vol(n):
    l = syracuse(n)
    rep = len(l)
    return rep-1 # on rajoute -1 pour ignorer la première étape

def altitude(n):
    l = syracuse(n)
    x = 0
    for i in l:
        if i > x:
            x = i
    return x

def max_vol(n):
    run = True
    i = 1
    while run:
        t = vol(i) # récupération de la longueur de vol
        if t > n:
            x = i
            run = False# coupe la boucle
        i += 1
    return x

def max_alti(n):
    run = True
    i = 1
    while run:
        t = altitude(i) # récupération de l'altitude la plus haurte
        if t > n:
            x = i
            run = False
        i += 1
    return x
















