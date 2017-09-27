import unittest
from apple import Apple

apple = Apple()

class AppleGetappleTest(unittest.TestCase):
    def test_word(self):
        self.assertEqual(apple.get_apple(), "apple")


if __name__ == '__main__':
    unittest.main()