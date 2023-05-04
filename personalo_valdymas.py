import os
import logging
import pickle
import json
from datetime import date

def create_logger(logger_name, log_file):
    # Logger'is
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    # Log handleris, kad pranešimai būtų išsaugomi į failą
    file_handler = logging.FileHandler(log_file, encoding = 'utf-8')
    file_handler.setLevel(logging.DEBUG)

    # Formatteris, kad pranešimai būtų formatuojami pagal pageidavimą
    formatter = logging.Formatter('%(asctime)s | Line: %(lineno)d | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)

    # Priskiriamas handleris loggeriui
    logger.addHandler(file_handler)

    return logger

logger = create_logger('logging', 'personalo_valdymas.log')
logger.info('Paleista programa')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

padaliniai = ["IT skyrius", "Finansai", "Administracija"]

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)

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
        self.__darbuotojai = {}
        self.__atleisti_darbuotojai = {}
        
    def prideti_darbuotoja(self, vardas_pavarde, komentaras, alga, priimtas, atleistas, tel_numeris, ak, issilavinimas, padalinys):
        darbuotojas = {'vardas_pavarde': vardas_pavarde, 'komentaras': komentaras, 'alga': alga, 'priimtas': priimtas, 'atleistas': atleistas, 'tel_numeris': tel_numeris, 'ak': ak, 'issilavinimas': issilavinimas, 'padalinys': padalinys}
        self.__darbuotojai[vardas_pavarde] = darbuotojas
        print(f"{vardas_pavarde} buvo pridėtas")
        logger.info(f'Pridėtas darbuotojas: "{vardas_pavarde}"')
        PersonaloValdymas.pickle_sukurimas(self)

    def atleisti_darbuotoja(self, vardas_pavarde, atleistas):
        darbuotojas = self.__darbuotojai.pop(vardas_pavarde, None)
        if darbuotojas:
            darbuotojas['atleistas'] = atleistas
            self.__atleisti_darbuotojai[vardas_pavarde] = darbuotojas
            logger.info(f'Atleistas darbuotojas: "{vardas_pavarde}"')
            PersonaloValdymas.pickle_sukurimas(self)

    def keisti_vardas(self, vardas_pavarde, naujas_vardas):
        darbuotojas = self.__darbuotojai.pop(vardas_pavarde, None)
        if darbuotojas:
            vardas, pavarde = vardas_pavarde.split()
            vardas = naujas_vardas
            darbuotojas['vardas_pavarde'] = vardas + " " + pavarde
            logger.info(f'Pakeistas darbuotojas vardas. Naujas vardas ir pavardė: "{vardas} {pavarde}"')
            self.__darbuotojai[darbuotojas['vardas_pavarde']] = darbuotojas
            PersonaloValdymas.pickle_sukurimas(self)
            return darbuotojas['vardas_pavarde']      
              
    def keisti_pavarde(self, vardas_pavarde, nauja_pavarde):
        darbuotojas = self.__darbuotojai.pop(vardas_pavarde, None)
        if darbuotojas:
            vardas, pavarde = vardas_pavarde.split()
            pavarde = nauja_pavarde
            darbuotojas['vardas_pavarde'] = vardas + " " + pavarde
            logger.info(f'Pakeistas darbuotojas vardas. Naujas vardas ir pavardė: "{vardas} {pavarde}"')
            self.__darbuotojai[darbuotojas['vardas_pavarde']] = darbuotojas
            PersonaloValdymas.pickle_sukurimas(self)
            return darbuotojas['vardas_pavarde']  

    def keisti_komentara(self,vardas_pavarde, komentaras):
        darbuotojas = self.__darbuotojai.get(vardas_pavarde)
        if darbuotojas is None:
            print(f"Darbuotojas {vardas_pavarde} nerastas")
        else:
            darbuotojas['komentaras'] = komentaras
            logger.info(f'Pakeistas darbuotojo "{vardas_pavarde}" komentaras"')
            PersonaloValdymas.pickle_sukurimas(self)
            return darbuotojas['vardas_pavarde'] 

    def keisti_alga(self, vardas_pavarde, alga):
        darbuotojas = self.__darbuotojai.get(vardas_pavarde)
        if darbuotojas is None:
            print(f"Darbuotojas {vardas_pavarde} nerastas")
        else:
            darbuotojas['alga'] = alga
            logger.info(f'Pakeista darbuotojo "{vardas_pavarde}" alga.')
            PersonaloValdymas.pickle_sukurimas(self)
            return darbuotojas['vardas_pavarde'] 

    def keisti_telefona(self, vardas_pavarde, tel_numeris):
        darbuotojas = self.__darbuotojai.get(vardas_pavarde)
        if darbuotojas is None:
            print(f"Darbuotojas {vardas_pavarde} nerastas")
        else:
            darbuotojas['tel_numeris'] = tel_numeris
            logger.info(f'Pakeistas darbuotojo "{vardas_pavarde}" tel_numeris')
            PersonaloValdymas.pickle_sukurimas(self)
            return darbuotojas['vardas_pavarde'] 

    def keisti_padalinys(self, vardas_pavarde, padalinys):
        darbuotojas = self.__darbuotojai.get(vardas_pavarde)
        if darbuotojas is None:
            print(f"Darbuotojas {vardas_pavarde} nerastas")
        else:
            darbuotojas['padalinys'] = padalinys
            logger.info(f'Pakeistas darbuotojo "{vardas_pavarde}" padalinys')
            PersonaloValdymas.pickle_sukurimas(self)
            return darbuotojas['vardas_pavarde'] 

    def darbuotoju_sarasas(self):
        print("Darbuotoju sarasas")
        print(list(self.__darbuotojai.values()))
        with open('Darbuotoju_sarasas.json', 'w') as f:
            json.dump(self.__darbuotojai, f, indent=4)
        logger.info('Darbas su failu: "Darbuotoju_sarasas.json"')
        return list(self.__darbuotojai.values())

    def get_darbuotojai(self):
        return self.__darbuotojai

    def get_darbuotojas(self, vardas_pavarde):
        return self.__darbuotojai.get(vardas_pavarde, None)
    
    def atleisti_darbuotojai(self):
        return self.__atleisti_darbuotojai
    
    def atleistu_darbuotoju_sarasas(self):
        print("Atleistu darbuotoju sarasas")
        print(list(self.__atleisti_darbuotojai.values()))
        with open('Atleistu_darbuotoju_sarasas.json', 'w') as f:
            json.dump(self.__atleisti_darbuotojai, f, indent=4, cls=DateEncoder)
            logger.info(f'Darbas su failu: "Atleistu_darbuotoju_sarasas.json"')
        return list(self.__atleisti_darbuotojai.values())

    def pickle_sukurimas(self):
        with open("Darbuotoju_duomenys.pickle", "wb") as f:
            pickle.dump(self.__darbuotojai, f)
            pickle.dump(self.__atleisti_darbuotojai, f)
            logger.info('Pickle sukūrinmas')
        return self
    
    def pickle_nuskaitymas(self):
        with open('Darbuotoju_duomenys.pickle', 'rb') as f:
            self.__darbuotojai = pickle.load(f)
            self.__atleisti_darbuotojai = pickle.load(f)
            logger.info('Pickle nuskaitymas')
        return self

# if __name__ == "__main__":
darbuotojai = PersonaloValdymas()
darbuotojai = PersonaloValdymas.pickle_nuskaitymas(darbuotojai)
# darbuotojai.prideti_darbuotoja("Algis Algimantas", "sokejas", 1111, "2002-05-12", None, "1234567988", "987654321", "traktoristas", "it")
# darbuotojai.prideti_darbuotoja("Algimante Algimantas", "sokejas", 1111, "2002-05-12", None, "1234567988", "987654321", "traktoristas", "it")
# darbuotojai.darbuotoju_sarasas()
# darbuotojai.atleisti_darbuotoja("Algis Algimantas", "2023-05-02")
# darbuotojai.atleisti_darbuotoja("Algimante Algimantas", "2023-05-02")
# darbuotojai.darbuotoju_sarasas()
# darbuotojai.atleistu_darbuotoju_sarasas()
# darbuotojai.keisti_alga("Algimante Algimantas", 2555)
# darbuotojai.keisti_alga("Algimante Algimantas", 1478)
# darbuotojai.darbuotoju_sarasas()

# darbuotojai.keisti_vardas("Algis Algimantas", "Pienius")
# darbuotojai.darbuotoju_sarasas()

# logger.info('Programa išjungta')
# darbuotojai.keisti_vardas("Algis Algimantas", "Pienius")
# darbuotojai.darbuotoju_sarasas()

print(darbuotojai._PersonaloValdymas__darbuotojai)

