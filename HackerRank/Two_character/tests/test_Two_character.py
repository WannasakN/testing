from code.Two_character import twoCharacter

import unittest

class TestTwoCharacter(unittest.TestCase):
    def test_give_abacabadabacaba_to_two_character(self):
        text = 'abacabadabacaba'
        expected_output = 3
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')


    def test_give_aabbcc_to_two_character(self):
        text = "aabbcc"
        expected_output = 0
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_aaaabbbb_to_two_character(self):
        text = "aaaabbbb"
        excecpted_output = 0
        result = twoCharacter(text)
        self.assertEqual(result, excecpted_output, f'Should be {excecpted_output}')

    def test_give_abcde_to_two_character(self):
        text = 'abcde'
        expected_output = 2
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_longtext_187_to_two_character(self):
        text = 'ThequickbrownfoxjumpsoverthelazydogLoremipsumdolorsitametconsecteturadipiscingelitPhasellusfringillamassaegetfringillaultricesnibhipsumullamcorperenimsitametcursusminislnislgetmagna'
        expected_output = 3
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
