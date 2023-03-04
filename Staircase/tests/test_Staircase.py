from code.Staircase import staircase

import unittest


class TestStaircase(unittest.TestCase):
    def test_give_0_staircase(self):
        n = 0
        printed_sym = '#'
        expected_output = ''

        result = staircase(n,printed_sym)

        self.assertEqual(result,expected_output)

    def test_give_1_staircase(self):
        n = 1
        printed_sym = '#'
        expected_output = '#'

        result = staircase(n,printed_sym)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_give_2_staircase(self):
        n = 2
        printed_sym = '#'
        expected_output = ' #\n' + \
        '##\n'

        result = staircase(n,printed_sym)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_3_staircase(self):
        n = 3
        printed_sym = '#'
        expected_output = '  #\n' + \
                    ' ##\n' + \
                    '###\n'

        result = staircase(n,printed_sym)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_30_staircase(self):
        n = 10
        printed_sym = '#'
        
        expected_output = '         #\n' + \
                  '        ##\n' + \
                  '       ###\n' + \
                  '      ####\n' + \
                  '     #####\n' + \
                  '    ######\n' + \
                  '   #######\n' + \
                  '  ########\n' + \
                  ' #########\n' + \
                  '##########\n'
        
        result = staircase(n,printed_sym)

        self.assertEqual(result, expected_output, f'Should be {expected_output}')

