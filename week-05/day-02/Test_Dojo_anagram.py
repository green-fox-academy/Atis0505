#Anagram test
import unittest
from Dojo_Anagram import check_is_anagram

class TestAnagram(unittest.TestCase): 
    def test_check_same_length_words(self):
        self.assertTrue(check_is_anagram("apple", "apple")) 
    
    def test_words_not_same_length_words(self):
        self.assertFalse(check_is_anagram("apple", "banana"))

    def test_check_sorted_words(self):
        self.assertTrue(check_is_anagram("cu", "uc"))

    def test_check_not_same_sorted_words(self):
        self.assertFalse(check_is_anagram("cs", "uc"))

    def test_null_words(self):
        self.assertEqual(check_is_anagram("",""),-1)

    def test_real_anagram(self):
        self.assertTrue(check_is_anagram("motherinlaw", "hitlerwoman"))

    def test_lower_case(self):
        self.assertTrue(check_is_anagram("Motherinlaw", "Hitlerwoman"))


if __name__ == '__main__':
    unittest.main()