import unittest
import count_letter

class CountLetterTest(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(count_letter.count_letter(""), {})


    def test_one_letter(self):
        self.assertEqual(count_letter.count_letter("a"), {"a":1})

    
    def test_two_letters(self):
        self.assertEqual(count_letter.count_letter("ab"), {"a":1, "b":1})


    def test_same_letters(self):
        self.assertEqual(count_letter.count_letter("aa"), {"a":2})


    def test_lot_letters(self):
        self.assertEqual(count_letter.count_letter("aaabbbbb"), {"a":3, "b":5})


if __name__ == "__main__":
    unittest.main()