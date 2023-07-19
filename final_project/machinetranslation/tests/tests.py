import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        # Test when 'Hello' given as input the output is 'Bonjour'.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        # Test when 'Bonjour' given as input the output is 'Hello'.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()
