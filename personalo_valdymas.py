import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Darbuotojas():
    def __init__(self, darbuotojas, komentaras):
        self.darbuotojas = darbuotojas
        self.komentaras = komentaras

class Personalo_Valdymas():
    def __init__(self):
        pass


