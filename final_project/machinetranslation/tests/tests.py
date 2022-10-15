import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(french_to_english(""))  # test when input text is empty
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when input text is valid

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(english_to_french(""))  # test when input text is empty
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when input text is valid

unittest.main()