import unittest

def divide(x, y):
    return x / y


class TestAssertMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5, "nelygus")

    def test_assertTrue(self):
        self.assertTrue(3 < 4, "neteisinga")

    def test_assertFalse(self):
        self.assertFalse(3 > 4, "turi buti neteisingai")

    def test_assertIs(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)

    def test_assertIsNone(self):
        self.assertIsNone(None)

    def test_integer_division(self):
        self.assertEqual(divide(10, 5), 10 // 5)


class MyClass:
    def __init__(self, x):
        self.x = x

    def add(self, y):
        self.x += y
        return self.x


class TestMyClass(unittest.TestCase):
    def setUp(self): 
        self.obj = MyClass(5)
        self.obj.add(5)

    def test_add(self):
        self.assertEqual(self.obj.add(3), 13)

    def test_add_more(self):
        self.assertEqual(self.obj.add(5), 15)
        self.assertEqual(self.obj.add(-10), 5)


if __name__ == "__main__":
    unittest.main()
