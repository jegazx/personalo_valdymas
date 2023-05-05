import unittest
from personalo_valdymas import PersonaloValdymas, Darbuotojas

class TestPersonaloValdymas(unittest.TestCase):
    def setUp(self):
        self.obj = PersonaloValdymas()
        self.obj.prideti_darbuotoja("Algis Algimantas", "Etatinis tinginys", 2000, "2018-05-16", 456789321, "78946855", "santechnikas", "traktoristas", None)
        self.obj.prideti_darbuotoja("Briedis Briedinskas", "Misko nususelis laukiantis medziokles sezono", 250, "2020-01-20)", 123456789, "10000001", "Pro zoles edikas", "Edikai", None)
        self.obj.prideti_darbuotoja("Lape Lapute", "Sukta brukta", 5000, "2018-05-10", 8888529, "100478001", "Sukciu", "IT specialybe", None)
        self.obj.prideti_darbuotoja("Kiskis Piskis", "Suolininkas", 500, "2012-07-22", "199999999", "91111111", "Atletika", "Buchalteris", None)

    def test_prideti_darbuotoja(self):
        self.obj.prideti_darbuotoja("Tomas Tomaitis", "programuotojas", 2500, "2021-09-01", "123456789", "987654321", "informatikos inžinierius", "IT skyrius", None)
        darbuotojas = self.obj.get_darbuotojas("Tomas Tomaitis")
        self.assertEqual(darbuotojas["vardas_pavarde"], "Tomas Tomaitis")

    def test_atleisti_darbuotoja(self):
        self.obj.atleisti_darbuotoja("Lape Lapute", "2023-04-10")
        darbuotojas = self.obj.get_darbuotojas("Lape Laputeq")
        self.assertIsNone(darbuotojas)

    def test_keisti_vardas(self):
        self.obj.keisti_vardas("Kiskis Piskis", "Ilgaausis")
        nauju_vardu = self.obj.get_darbuotojas("Ilgaausis Piskis")
        self.assertEqual(nauju_vardu["vardas_pavarde"], "Ilgaausis Piskis")

    def test_keisti_pavarde(self):
        self.obj.keisti_pavarde("Briedis Briedinskas", "Edikas")
        nauja_pavarde = self.obj.get_darbuotojas("Briedis Edikas")
        self.assertEqual(nauja_pavarde["vardas_pavarde"], "Briedis Edikas")
    
    def test_keisti_komentara(self):
        self.obj.keisti_komentara("Algis Algimantas", "Geras darbuotojas")
        darbuotojas = self.obj.get_darbuotojas("Algis Algimantas")
        self.assertEqual(darbuotojas["komentaras"], "Geras darbuotojas")

    def test_keisti_alga(self):
        self.obj.keisti_alga("Algis Algimantas", 4000)
        darbuotojas = self.obj.get_darbuotojas("Algis Algimantas")
        self.assertEqual(darbuotojas["alga"], 4000)

    def test_keisti_telefona(self):
        self.obj.keisti_telefona("Lape Lapute", "123456789")
        darbuotojas = self.obj.get_darbuotojas("Lape Lapute")
        self.assertEqual(darbuotojas["tel_numeris"], "123456789")
    
    def test_keisti_padalinys(self):
        self.obj.keisti_padalinys("Briedis Briedinskas", "Apsauginis")
        darbuotojas = self.obj.get_darbuotojas("Briedis Briedinskas")
        self.assertEqual(darbuotojas["padalinys"], "Apsauginis")



if __name__ == "__main__":
    unittest.main()
