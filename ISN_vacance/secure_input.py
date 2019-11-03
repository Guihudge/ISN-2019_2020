def input_secure(text=""):  # permet d'éviter les erreur de convertion en nombre.
    while True:
        try:
            rep = int(input(text))
            break
        except ValueError:  # permet d'éviter l'erreur de conviertion str -> int
            print("Veuillez rentrer un chiffre SVP.")
    return rep