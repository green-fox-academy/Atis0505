import unittest
import anagram

class AnagramTest(unittest.TestCase):
    def test_leng_of_words(self):
        self.assertTrue(anagram.check_words("alma","amla"), True)
    

    def test_different_leng_words(self):
        self.assertFalse(anagram.check_words("aasd","adfds"))


    def test_is_not_anagram_words(self):
        self.assertFalse(anagram.check_words("alma", "baba"))
    
if __name__ == "__main__":
    unittest.main()