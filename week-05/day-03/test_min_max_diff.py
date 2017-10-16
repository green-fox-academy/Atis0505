import unittest
from min_max_diff import min_max_diff


class TestMinimumMaximumDiff(unittest.TestCase):
    def test_diff_between_max_and_min_numbers(self):
        self.assertEqual(min_max_diff([0, 2, 3]), 3)

    def test_one_element(self):
        self.assertEqual(min_max_diff([0]), 0)

    def test_none_type(self):
        self.assertFalse(min_max_diff([]))

    


if __name__ == '__main__':
    unittest.main()