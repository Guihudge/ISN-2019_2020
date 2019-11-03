# transforme un texte en image

from PIL import Image
from math import ceil, sqrt

file = open("text.txt", 'r')  # Ouverture du fichier contenant l'image
msg = file.read()  # écrit l'intégralité du fichier dans la variable
len_msg = len(msg)

x = ceil(sqrt(len_msg))  # On détermine la taille de l'image
y = ceil(len_msg/x)

img = Image.new("L", (x, y))  # on créer l'image en mode noir et blanc

x_encode = 0  # init de l'encodage
y_encode = 0

for i in msg:
    color = ord(i)  # on détremine la couleur du pixel grâce à la valeur ASCII du caractère
    img.putpixel((x_encode, y_encode), color)  # on code la couleur sur la pixel voulue
    x_encode += 1  # on passe au pixel suivant
    if x_encode == x:
        x_encode = 0
        y_encode += 1

img.save("test.png")  # on sauvegarde l'image


