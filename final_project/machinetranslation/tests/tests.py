import unittest
from translator import french_to_english,english_to_french

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish_1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hi")

    def test_frenchToEnglish_2(self):
        self.assertEqual(french_to_english("Arbre"),"Tree")

    def test_englishToFrench_1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    
    def test_englishToFrench_2(self):
        self.assertEqual(english_to_french("Tree"),"Arbre")


if __name__ == "__main__":
    unittest.main()