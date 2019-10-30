def input_secure(text=""):
    while True:
        try:
            rep = int(input(text))
            break
        except ValueError:
            print("Veuillez rentrer un chiffre SVP.")
    return rep