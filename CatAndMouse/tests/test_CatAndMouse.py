from code.CatAndMouse import CatAndMouse

import unittest

class TestCatAndMouse(unittest.TestCase):
    def test_1_2_3_in_CatMouse(self): 
        result = CatAndMouse(1,2,3)
        self.assertEqual(result, 'Cat B')

    def test_1_3_2_in_CatMouse(self): 
        result = CatAndMouse(1,3,2)
        self.assertEqual(result, 'Mouse C')

    def test_5_1_6_in_CatMouse(self): 
        result = CatAndMouse(5,1,6)
        self.assertEqual(result, 'Cat A')

    def test_9_10_100_in_CatMouse(self): 
        result = CatAndMouse(9,10,100)
        self.assertEqual(result, 'Cat B')
    
    def test_n1_5_2_in_CatMouse(self): 
        result = CatAndMouse(-1,5,2)
        self.assertEqual(result, 'Mouse C')
