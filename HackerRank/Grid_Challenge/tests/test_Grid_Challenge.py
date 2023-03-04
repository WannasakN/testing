from code.Grid_Challenge import gridChallenge

import unittest

class TestGridChallenge(unittest.TestCase):
    def test_give_exampleList_1_to_grid(self): #เทสด้วยตัวอักษรเดียวกันในหลายแถว
        lst = ['aaa', 'aaa', 'aaa']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_2_to_grid(self): #เทสด้วยตัวอักษรแบบสุ่มในหลายแถว ไม่เรียงลำดับ
        lst = ['bad', 'cab', 'dac']
        expected_output = 'NO'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output , f'Shoud be {expected_output}')

    def test_give_exampleList_3_to_grid(self): #เทสด้วยตัวอักษรเดียว
        lst = ['a']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_4_to_grid(self): #เทสด้วยอักษรพิเศษ
        lst = ['$#@', '!*&', '^%$']
        expected_output = 'NO'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_5_to_grid(self): #เทสด้วยตัวอักษรแบบสุ่มในหลายแถว เรียงลำดับจากมากไปน้อย
        lst = ['ihg', 'fed', 'cba']
        expected_output = 'NO'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')
