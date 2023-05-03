import unittest
from personalo_valdymas import PersonaloValdymas, Darbuotojas


class TestPersonaloValdymas(unittest.TestCase):

    def setUp(self):
        self.obj = PersonaloValdymas()
        self.obj.prideti_darbuotoja("Algis Algimantas", "Etatinis tinginys", 2000, "2018-05-16", None, 456789321, "78946855", "santechnikas", "traktoristas")
        self.obj.prideti_darbuotoja("Briedis Briedinskas", "Misko nususelis laukiantis medziokles sezono", 250, "2020-01-20", None, 123456789, "10000001", "Pro zoles edikas", "Edikai")
        
    def test_prideti_darbuotoja(self):
        self.obj.prideti_darbuotoja("Briedis Briedinskas", "Misko nususelis laukiantis medziokles sezono", 250, "2020-01-20", None, 123456789, "10000001", "Pro zoles edikas", "Edikai")
        self.assertEqual("Briedis Briedinskas", "Briedis Briedinskas")



    def test_atleisti_darbuotoja(self):
        self.obj.atleisti_darbuotoja("Algis Algimantas", "2020-05-23")
        self.assertEqual("Algis Algimantas", "Algis Algimantas")






if __name__ == "__main__":
    unittest.main()