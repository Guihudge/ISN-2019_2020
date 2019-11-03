import os
import sys
from secure_input import input_secure


def liste_file(extension):  # crée une liste de fichier avec l'extention demander
    liste_fichier = os.listdir()  # liste tout le fichier du répertoire
    fichier = []

    for i in range(0, len(liste_fichier)):
        name, ext = os.path.splitext(liste_fichier[i])  # récupère l'extention du fichier

        if ext == extension:  # ajoute le fichier à la liste si l'extention est correcte
            fichier.append(liste_fichier[i])

    return fichier  # retourne la liste de fichier avec l'extention demander


def choix_fichiers(extenssion):
    file = liste_file(extenssion)

    if len(file) == 0:
        error = "Auccun fichier " + extenssion + " détecter, veulliez en rajouter un dans le répertoire " \
                                                 "du programme puis le relancer."  # création de la chaine d'érreur
        sys.exit(error)  # quitte le programe avec l'erreur donner

    while True:  # Affichage du résultat + chois de ce résultat

        for i in range(0, len(file)):
            print(i+1, ":", file[i])

        rep = input_secure("\nQuel fichier voulez vous utiliser? ")

        try:
            return file[rep-1]
        except IndexError:  # Oblige l'utilisateur à choisir un nombre proposé.
            print("Merci de renter un nombre proposé")


def outfile(extenssion):
    while True:
        output = input("Nom du fichier de sortie (il peut exister ou pas): ")

        if output == "":
            print("Veuillez rentrer un nom SVP.")
        else:
            break

    if output[-4:] != extenssion:  # ajoute l'extention au fichier si l'utilisateur ne la pas mis ou pas la bonne
        output = output + extenssion

    return output
