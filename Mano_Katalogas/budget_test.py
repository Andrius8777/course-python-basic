import unittest


def test_prideti_iplaukas_islaidas(self):
    self.biudzetas.add("kazkas", 10)
    self.assertEqual(self.biudzetas.pavadinimas["kazkas"], 2)



from budgetlt import prideti_iplaukas_islaidas

class Testprideti_iplaukas_islaidas(unittest.TestCase):
