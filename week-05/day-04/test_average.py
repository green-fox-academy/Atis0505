import unittest
from average import odd_average


class TestAverage(unittest.TestCase):
    def test_one_number(self):
        self.assertEqual(odd_average([4]), 4)

    def test_two_numbers(self):
        self.assertEqual(odd_average([3,5]), 4)    

    def test_empty_list(self):
        self.assertEqual(odd_average([]), 0)


if __name__ == '__main__':
    unittest.main()