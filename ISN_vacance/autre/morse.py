import winsound
from time import sleep


def point():
    winsound.Beep(500, 100)


def tirait():
    winsound.Beep(500, 300)


def entre_tirret_point():
    sleep(0.100)


def entre_lettre():
    sleep(0.300)


def entre_mot():
    sleep(0.700)


morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
         '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
         '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
         ')': '-.--.-'}

def ecrypt(message):
    for lettre in message:
        if lettre == " ":
            entre_mot()
        else:
            code = morse[lettre]
            for beep in code:
                print(beep)
                if beep == ".":
                    point()
                else:
                    tirait()
            entre_tirret_point()
        entre_lettre()

msg = input("message?")

ecrypt(msg.upper())
