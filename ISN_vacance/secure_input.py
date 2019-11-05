def input_secure(text=""):  # permet d'éviter les erreurs de convertion en nombre.
    while True:
        try:
            rep = int(input(text))
            break
        except ValueError:  # permet d'éviter l'erreur de convertion str -> int
            print("Veuillez rentrer un chiffre SVP.")
    return rep
