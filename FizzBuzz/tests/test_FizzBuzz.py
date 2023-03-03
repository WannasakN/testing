from code.Fizzbuzz import Fizzbuzz

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_3_in_FizzBuzz(self): #เทสด้วยเลข 3
        self.assertEqual(Fizzbuzz(3), 'Fizz')

    def test_5_in_FizzBuzz(self): #เทสด้วยเลข 5
        self.assertEqual(Fizzbuzz(5), 'buzz')
    
    def test_9_in_FizzBuzz(self): #เทสด้วยเลขที่หายด้วย 3 ลงตัว
        self.assertEqual(Fizzbuzz(9), 'Fizz')
    
    def test_10_in_FizzBuzz(self): #เทสด้วยเลขที่หายด้วย 5 ลงตัว
        self.assertEqual(Fizzbuzz(10), 'buzz')
    
    def test_15_in_FizzBuzz(self):  #เทสด้วยเลขที่หายด้วย 3 และ 5 ลงตัว 
        self.assertEqual(Fizzbuzz(15), 'Fizzbuzz')
