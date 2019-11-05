import os
import sys
from secure_input import input_secure


def liste_file(extension):  # crée une liste de fichiers avec l'extension demandée
    liste_fichier = os.listdir()  # liste tout le fichier du répertoire
    fichier = []

    for i in range(0, len(liste_fichier)):
        name, ext = os.path.splitext(liste_fichier[i])  # récupère l'extension du fichier

        if ext == extension:  # ajoute le fichier à la liste si l'extension est correcte
            fichier.append(liste_fichier[i])

    return fichier  # retourne la liste de fichier avec l'extension demandée


def choix_fichiers(extenssion):
    file = liste_file(extenssion)

    if len(file) == 0:
        error = "Aucun fichier " + extenssion + " détecté, veuillez en rajouter un dans le répertoire " \
                                                 "du programme puis le relancer."  # création de la chaine d'erreur
        sys.exit(error)  # quitte le programe avec l'erreur donnée

    while True:  # Affichage du résultat + choix de ce résultat

        for i in range(0, len(file)):
            print(i+1, ":", file[i])

        rep = input_secure("\nQuel fichier voulez-vous utiliser? ")

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

    if output[-4:] != extenssion:  # ajoute l'extension au fichier si l'utilisateur ne l'a pas mise ou pas n'est pas la bonne
        output = output + extenssion

    return output
