import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 1)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(1, 1), 2)


if __name__ == '__main__':
    unittest.main()