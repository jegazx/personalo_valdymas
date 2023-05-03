import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


padaliniai = ["IT skyrius", "Finansai", "Administracija"]


class Darbuotojas():
    def __init__(self, vardas_pavarde, komentaras, alga, priimtas, atleistas, tel_numeris, ak, issilavinimas, padalinys):
        self.vardas_pavarde = vardas_pavarde
        self.komentaras = komentaras
        self.alga = alga
        self.priimtas = priimtas
        self.atleistas = atleistas
        self.tel_numeris = tel_numeris
        self.ak = ak
        self.issilavinimas = issilavinimas
        self.padalinys = padalinys

class PersonaloValdymas():
    def __init__(self):
        self.darbuotojas = []
        

    def prideti_darbuotoja(self, vardas_pavarde, komentaras, alga, priimtas, atleistas, tel_numeris, ak, issilavinimas, padalinys):
        pass

    def atleisti_darbuotoja(self, vardas_pavarde, atleistas):
        pass

    def keisti_vardas(self, vardas_pavarde):
        pass

    def keisti_pavarde(self, vardas_pavarde):
        pass

    def keisti_komentara(self,vardas_pavarde, komentaras):
        pass

    def keisti_alga(self, vardas_pavarde, alga):
        pass

    def keisti_telefona(self, vardas_pavarde, tel_numeris):
        pass

    def keisti_padalinys(self, vardas_pavarde, padalinys):
        pass

    def darbuotoju_sarasas(self):
        pass

