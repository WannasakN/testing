from code.Funny_string import funnyString

import unittest

class TestFunnyString(unittest.TestCase):
    def test_acxz_in_FunnyString(self):
        x = 'acxz'
        result = funnyString(x)
        self.assertEqual(result,'Funny')
        
    def test_dgdfnfnf_in_FunnyString(self):
        x = 'dgdfnfnf'
        result = funnyString(x)
        self.assertEqual(result,'Not Funny')

    def test_abcd_in_FunnyString(self):
        x = 'abcd'
        result = funnyString(x)
        self.assertEqual(result,'Funny')
    
    def test_qmst_in_FunnyString(self):
        x = 'qmst'
        result = funnyString(x)
        self.assertEqual(result,'Not Funny')
        
    def test_mnop_in_FunnyString(self):
        x = 'mnop'
        result = funnyString(x)
        self.assertEqual(result,'Funny')
