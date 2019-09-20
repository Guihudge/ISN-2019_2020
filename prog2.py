import math

def premierdegre (a,b):
    if a == 0: # empèche la division par zero
        print("pas de solution")	
    else:
        print("solution :", float(b/a))


def trinome (a, b, c):
    d = (b*b)-4*(a*c)

    if a == 0: # vérifie si c'est bien un trinome du second degré
        print("ce n'est pas un trinome du second degré")
        return
    
    if d > 0:
        print("deux solution", (-b-math.sqrt(d))/(2*a), (-b+math.sqrt(d))/(2*a))
    elif d == 0:
        print("une seul solution", -b/2*a)
    else:
        print("pas de solution")

def multi (a):
    x= int(input("valeur max de la table: "))
    
    for i in range(0,x+1):
        print(str(a)+ " x "+ str(i)+ " = " + str(a*i))
def suite (n):
    # U0 = 1
    # Un+1 = 3Un +2
    U = 1
    print("U0"+" = " + str(U))
    for i in range(1, n):
        n = 3*U + 2
        print("U"+str(i) + " = " + str(n))
        U = n

def suite_bis (x):
    # U0 = 1
    # Un+1 = 3Un +2
    U = 1
    # print("U0"+" = " + str(U))
    for i in range(1, x):
        n = 3*U + 2
        # print("U"+str(i) + " = " + str(n))
        U = n
    print("U"+str(x) + " = " + str(U))

def somme (n):
    # somme(3) = 1+2+3
    l = []
    x=0
    for i in range(n+1):
        l.append(i)
    # print(l)
    
    print(math.fsum(l))

def factoriel(n):
    for i in range(n+1):
        print(math.factorial(i))

def factoriel_bis (n):
    # somme(3) = 1+2+3
    l = []
    x=1
    for i in range(1, n+1):
        l.append(i)
    # print(l)
    
    for i in l:
        x = x*i
        print(x)

