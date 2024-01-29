import unittest

class Calculator:
    def add(self, x, y):
        rez = x + y
        if x > 5 and y < 0:
            print(f"{x} turi buti daugiau uz 5, {y} turi buti maziau uz 0")
        else:
            return rez
         
        

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        # Test addition of positive numbers
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)

        # Test case with x > 5 and y < 0
        with self.assertRaises(ValueError):
            self.calc.add(6, -1)

        # Test case with x <= 5 and y < 0
        result = self.calc.add(5, -2)
        self.assertEqual(result, 3)

        # Test case with x > 5 and y >= 0
        result = self.calc.add(6, 2)
        self.assertEqual(result, 8)

        # Test case with x <= 5 and y >= 0
        result = self.calc.add(4, 2)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()