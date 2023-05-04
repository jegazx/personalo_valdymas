import unittest
from datetime import date
from personalo_valdymas import PersonaloValdymas, Darbuotojas


class TestPersonaloValdymas(unittest.TestCase):

    def setUp(self):
        self.obj = PersonaloValdymas()
        self.obj.prideti_darbuotoja("Algis Algimantas", "Etatinis tinginys", 2000, date(2018, 5, 16), None, 456789321, "78946855", "santechnikas", "traktoristas")
        self.obj.prideti_darbuotoja("Briedis Briedinskas", "Misko nususelis laukiantis medziokles sezono", 250, date(2020, 1, 20), None, 123456789, "10000001", "Pro zoles edikas", "Edikai")
        self.obj.prideti_darbuotoja("Lape Lapute", "Sukta brukta", 5000, date(2018, 5, 10), None, 8888529, "100478001", "Sukciu", "IT specialybe")


    def test_prideti_darbuotoja(self):
        self.obj.prideti_darbuotoja("Kiskis Piskis", "Suolininkas", 500, date(2012, 7, 22), None, "199999999", "91111111", "Atletika", "Buchalteris")
        sukurtas_darbuotojas = self.obj.get_darbuotojas("Kiskis Piskis")
        self.assertEqual(sukurtas_darbuotojas.komentaras, "Suolininkas")

    # def test_atleisti_darbuotoja(self):
    #     self.obj.atleisti_darbuotoja("Lape Lapute", date.today())
    #     self.assertEqual(len(self.obj.darbuotojai), 0)
    #     self.assertEqual(len(self.obj.atleisti_darbuotojai), 1)

    # def test_keisti_vardas(self):
    #     self.keisti_vardas("Briedis Briedinskas", "Snapinskas")

if __name__ == "__main__":
    unittest.main()
