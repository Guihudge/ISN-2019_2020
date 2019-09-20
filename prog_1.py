import math

def aire_rectangle (L, l):
    result = L*l
    return result


def echanger(a,b):
    c = a
    a = b
    b = c
    return a,b


def echanger_bis(a,b):
    c =  b,a
    return c


def aire_cercle (r):
    a = math.pi * (r**2) # declaration variable a pour l aire du cercle a la quel on affacte pi*r**2
    return a


def pair (n):
    test = n%2
    if test == 1:
        return False
    else:
        return True


def signe (x):
    if x > 0:
        print(str(x) + " est strictement positif")
    elif x == 0:
        print(str(x) + " est nul")
    elif x < 0:
        print(str(x) + " est strictement negatif")

def maximum (a, b, c):
    L = []
    x = 0
    L.append(a)
    L.append(c)
    L.append(b)

    for i in L:
        if i > x:
            x = i
    return x

def maximum (a, b, c):
    if a>b and a>c:
        print("a plus grand")
    if b>a and b>c:
        print("b le plus grand")
        
##l = input("l? ")
##L = input("L? ")
##print("aire rectangle: "+ str(aire_rectangle(L,l)))
