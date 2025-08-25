import unittest
from main import karatsuba

class TestKaratsuba(unittest.TestCase):
    def test_small_numbers(self):
        for a in range(0, 20):
            for b in range(0, 20):
                self.assertEqual(karatsuba(a, b), a * b)

    def test_random(self):
        import random
        for _ in range(100):
            a = random.randrange(-10**50, 10**50)
            b = random.randrange(-10**50, 10**50)
            self.assertEqual(karatsuba(a, b), a * b)

if __name__ == '__main__':
    unittest.main()