import unittest
from sum import Sum

sum = Sum()

integ_list = [2,4,5]

class GetListSumTest(unittest.TestCase):
    def test_int_list(self):
        self.assertEqual(sum.get_sum(integ_list), 11)


    def test_null_list(self):
        self.assertEqual(sum.get_sum([]), 0)


    def test_one_item_in_list(self):
        self.assertEqual(sum.get_sum(3), '3')
    

    def test_null_value(self):
        self.assertEqual(sum.get_sum(None), None)
if __name__ == "__main__":
    unittest.main()