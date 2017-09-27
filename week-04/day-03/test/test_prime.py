import unittest
from prime import is_prime

class PrimeTestCases(unittest.TestCase):
    def test_three(self):
        self.assertTrue(is_prime(3))


    def test_two(self):
        self.assertTrue(is_prime(2))


    def test_big(self):
        self.assertTrue(is_prime(97))

    
    def test_one(self):
        self.assertFalse(is_prime(1))


if __name__ == '__main__':
    unittest.main()