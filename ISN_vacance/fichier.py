import os
from secure_input import input_secure


def liste_file(extension):
    liste_fichier = os.listdir()
    fichier = []

    for i in range(0, len(liste_fichier)):
        name, ext = os.path.splitext(liste_fichier[i])

        if ext == extension:
            fichier.append(liste_fichier[i])

    return fichier


def choix_fichiers(extenssion):
    file = liste_file(extenssion)
    while True:

        for i in range(0, len(file)):
            print(i+1, ":", file[i])

        rep = input_secure("\nQuel fichier voulez vous utiliser? ")

        try:
            return file[rep-1]
        except IndexError:
            print("Merci de renter un nombre proposé")

