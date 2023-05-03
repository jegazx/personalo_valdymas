import os
import logging

def create_logger(logger_name, log_file):
    # Logger'is
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    # Log handleris, kad pranešimai būtų išsaugomi į failą
    file_handler = logging.FileHandler(log_file, encoding = 'utf-8')
    file_handler.setLevel(logging.DEBUG)

    # Formatteris, kad pranešimai būtų formatuojami pagal pageidavimą
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Priskiriamas handleris loggeriui
    logger.addHandler(file_handler)

    return logger

logger = create_logger('logging', 'personalo_valdymas.log')
logger.info('Paleista programa')

import pickle


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
        self.__darbuotojai = []
        self.__atleisti_darbuotojai = []
        
    def prideti_darbuotoja(self, vardas_pavarde, komentaras, alga, priimtas, atleistas, tel_numeris, ak, issilavinimas, padalinys):
        darbuotojas = Darbuotojas(vardas_pavarde, komentaras, alga, priimtas, atleistas, tel_numeris, ak, issilavinimas, padalinys)
        self.__darbuotojai.append(darbuotojas)
        print(f"{darbuotojas} buvo pridetas")

        logger.info(f'Pridėtas darbuotojas: "{vardas_pavarde}"')

        PersonaloValdymas.pickle_sukurimas(darbuotojai)


    def atleisti_darbuotoja(self, vardas_pavarde, atleistas):
        for darbuotojas in self.__darbuotojai:
            if darbuotojas.vardas_pavarde == vardas_pavarde:
                self.__darbuotojai.remove(darbuotojas)
                darbuotojas.atleistas = atleistas

                self.atleisti_darbuotojai.append(darbuotojas)
                logger.info(f'Atleistas darbuotojas: "{vardas_pavarde}"')

                self.__atleisti_darbuotojai.append(darbuotojas)
                PersonaloValdymas.pickle_sukurimas(darbuotojai)

                break

    def keisti_vardas(self, vardas_pavarde, naujas_vardas):
        for darbuotojas in self.__darbuotojai:
            if darbuotojas.vardas_pavarde == vardas_pavarde:
                vardas, pavarde = vardas_pavarde.split()
                vardas = naujas_vardas
                darbuotojas.vardas_pavarde = vardas + " " + pavarde

                logger.info(f'Pakeistas darbuotojo vardas. Naujas vardas ir pavardė: "{vardas} {pavarde}"')

                PersonaloValdymas.pickle_sukurimas(darbuotojai)

                return vardas_pavarde
                
    def keisti_pavarde(self, vardas_pavarde, nauja_pavarde):
        for darbuotojas in self.__atleisti_darbuotojai:
            if darbuotojas.vardas_pavarde == vardas_pavarde:
                vardas, pavarde = vardas_pavarde.split
                pavarde = nauja_pavarde
                darbuotojas.vardas_pavarde = vardas + " " + pavarde

                logger.info(f'Pakeista darbuotojo pavardė. Naujas vardas ir pavardė: "{vardas} {pavarde}"')

                PersonaloValdymas.pickle_sukurimas(darbuotojai)

                return vardas_pavarde

    def keisti_komentara(self,vardas_pavarde, komentaras):
        for darbuotojas in self.__darbuotojai:
            if darbuotojas.vardas_pavarde == vardas_pavarde:
                darbuotojas.komentaras = komentaras

                logger.info(f'Pakeistas darbuotojo "{vardas_pavarde}" komentaras')

                PersonaloValdymas.pickle_sukurimas(darbuotojai)

                break

    def keisti_alga(self, vardas_pavarde, alga):
        for darbuotojas in self.__darbuotojai:
            if darbuotojas.vardas_pavarde == vardas_pavarde:
                darbuotojas.alga = alga

                logger.warning(f'Pakeista alga darbuotojui "{vardas_pavarde}". Nauja alga: {alga}')

                PersonaloValdymas.pickle_sukurimas(darbuotojai)

                break

    def keisti_telefona(self, vardas_pavarde, tel_numeris):
        for darbuotojas in self.__darbuotojai:
            if darbuotojas.vardas_pavarde == vardas_pavarde:
                darbuotojas.tel_numeris = tel_numeris

                logger.info(f'Pakeistas darbuotojo "{vardas_pavarde}" telefono Nr. Naujas telefono Nr.: {tel_numeris}')

                PersonaloValdymas.pickle_sukurimas(darbuotojai)

                break

    def keisti_padalinys(self, vardas_pavarde, padalinys):
        for darbuotojas in self.__darbuotojai:
            if darbuotojas.vardas_pavarde == vardas_pavarde:
                darbuotojas.padalinys = padalinys

                logger.info('Pakeistas padalinys')

                PersonaloValdymas.pickle_sukurimas(darbuotojai)

                break

    def darbuotoju_sarasas(self):
        if self.__darbuotojai:
            print("Darbuotoju sarasas: ")
            for darbuotojas in self.__darbuotojai:
                print(f"{darbuotojas.vardas_pavarde} - {darbuotojas.komentaras} - {darbuotojas.alga} - {darbuotojas.priimtas} - {darbuotojas.atleistas} - {darbuotojas.tel_numeris} - {darbuotojas.ak} - {darbuotojas.issilavinimas} - {darbuotojas.padalinys}")

        logger.info('Atspausdintas darbuotojų sąrašas')

    def atleisti_darbuotoju_sarasas(self):
        if self.atleisti_darbuotojai:

    
    def atleistu_darbuotoju_sarasas(self):
        if self.__atleisti_darbuotojai:

            print("Atleistu darbuotoju sarasas: ")
            for darbuotojas in self.__atleisti_darbuotojai:
                print(f"{darbuotojas.vardas_pavarde} - {darbuotojas.komentaras} - {darbuotojas.alga} - {darbuotojas.priimtas} - {darbuotojas.atleistas} - {darbuotojas.tel_numeris} - {darbuotojas.ak} - {darbuotojas.issilavinimas} - {darbuotojas.padalinys}")

        logger.info('Atspausdintas atleistų darbuotojų sąrašas')

    
    def pickle_sukurimas(duomenys):
        with open("Darbuotoju_duomenys.pickle", "wb") as file:
            pickle.dump(duomenys, file)
        return duomenys
    
    def pickle_nuskaitymas(duomenys):
        with open('Darbuotoju_duomenys.pickle', 'rb') as f:
            duomenys = pickle.load(f)
        return duomenys


darbuotojai = PersonaloValdymas()
darbuotojai = PersonaloValdymas.pickle_nuskaitymas(darbuotojai)
# darbuotojai.prideti_darbuotoja("Algis Algimantas", "sokejas", 1111, "2002-05-12", None, "1234567988", "987654321", "traktoristas", "it")
# darbuotojai.prideti_darbuotoja("Algimante Algimantas", "sokejas", 1111, "2002-05-12", None, "1234567988", "987654321", "traktoristas", "it")
# darbuotojai.darbuotoju_sarasas()
# darbuotojai.atleisti_darbuotoja("Algis Algimantas", "2023-05-02")
# darbuotojai.atleisti_darbuotoja("Algimante Algimantas", "2023-05-02")
# darbuotojai.darbuotoju_sarasas()
# darbuotojai.atleisti_darbuotoju_sarasas()
darbuotojai.keisti_alga("Algimante Algimantas", 2555)
# darbuotojai.darbuotoju_sarasas()

darbuotojai.keisti_vardas("Algis Algimantas", "Pienius")
darbuotojai.darbuotoju_sarasas()

logger.info('Programa išjungta')
# darbuotojai.keisti_vardas("Algis Algimantas", "Pienius")
# darbuotojai.darbuotoju_sarasas()

