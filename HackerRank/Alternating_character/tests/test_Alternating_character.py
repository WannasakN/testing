from code.Alternating_character import AlternatingCharacter

import unittest

class TestAlternatingCharacter(unittest.TestCase):
    def test_AAAAA_in_Alternating(self):
        x = 'AAAAA'
        result = AlternatingCharacter(x)
        self.assertEqual(result,4)

    def test_BBBBB_in_Alternating(self):
        x = 'BBBBB'
        result = AlternatingCharacter(x)
        self.assertEqual(result,4)

    def test_ABABABA_in_Alternating(self):
        x = 'ABABABA'
        result = AlternatingCharacter(x)
        self.assertEqual(result,0)

    def test_AAABBB_in_Alternating(self):
        x = 'AAABBB'
        result = AlternatingCharacter(x)
        self.assertEqual(result,4)
    
    def test_BBAABBAA_in_Alternating(self):
        x = 'BBAABBAA'
        result = AlternatingCharacter(x)
        self.assertEqual(result,4)
