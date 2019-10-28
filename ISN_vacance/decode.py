from PIL import Image

img = Image.open("test.png")  # on ouvre l'image contanant le texte

x, y = img.size  # on récupère le taille de l'image
file = open("output.txt", "w")  # on ouvre/crée le fichier de sortie

msg = ""

for y_decode in range(0, y):
    for x_decode in range(2, x):
        lettre = chr(img.getpixel((x_decode, y_decode)))  # on convertie la couleur en caractère
        msg = msg+lettre

file.write(msg)  # on écrit dans le fichier
file.close()  # on ferme le ficher
