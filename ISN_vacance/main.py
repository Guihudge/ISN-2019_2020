from math import ceil, sqrt
from sys import exit

from PIL import Image


def encode(file, output):
    file = open(file, 'r')  # Ouverture du fichier contenant le texte
    msg = file.read()  # écrit l'intégralité du fichier dans la variable
    len_msg = len(msg)

    x = ceil(sqrt(len_msg))  # On détermine la taille de l'image
    y = ceil(len_msg / x)

    img = Image.new("L", (x, y))  # on crée l'image en mode noir et blanc

    x_encode = 0  # init de l'encodage
    y_encode = 0

    for i in msg:
        color = ord(i)  # on détermine la couleur du pixel grâce à la valeur ASCII du caractère
        img.putpixel((x_encode, y_encode), color)  # on code la couleur sur la pixel voulue
        x_encode += 1  # on passe au pixel suivant
        if x_encode == x:
            x_encode = 0
            y_encode += 1

    try:
        img.save(output)  # on sauvegarde l'image
    except:
        output = output + ".jpg"
        img.save(output)


def decode(image, output):
    img = Image.open(image)  # on ouvre l'image contenant le texte

    x, y = img.size  # on récupère le taille de l'image
    file = open(output, "w")  # on ouvre/crée le fichier de sortie

    msg = ""

    for y_decode in range(0, y):
        for x_decode in range(2, x):
            lettre = chr(img.getpixel((x_decode, y_decode)))  # on convertie la couleur en caractère
            msg = msg + lettre

    file.write(msg)  # on écrit dans le fichier
    file.close()  # on ferme le ficher


def input_secure():
    while True:
        try:
            rep = int(input())
            break
        except ValueError:
            print("Veuillez rentrer un chiffre SVP.")
    return rep


def choix_file(type):
    # type = 1 -> encode; type = 2 -> decode
    if type == 1:
        file = input("Nom du fichier avec le texte à encoder (le nom doit être exacte!): ")
        output = input("Nom du fichier de sortie (il peut exister ou pas): ")
        encode(file, output)
    elif type == 2:
        image = input("Nom de l'image avec le texte à décoder (le nom doit être exacte!): ")
        output = input("Nom du fichier de sortie (il peut exister ou pas): ")
        decode(image, output)


def intro():
    print("Programme d'encodage de texte sous forme d'image et de décodage")


def menu():
    print("Que voulez vous faire?")
    print("1) Encoder un texte sous forme d'image")
    print("2) Décoder une image sous forme de texte")
    print("3) Quitter")

    rep = input_secure()
    if rep == 1:
        choix_file(1)
    elif rep == 2:
        choix_file(2)
    else:
        exit(1)


def run():
    intro()
    while True:
        menu()


run()
