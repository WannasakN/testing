from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_6_8_is_not_primes(self): 
        prime_list = [4,6,8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    
    def test_give_5_5_5_is_prime(self): 
        prime_list = [5,5,5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_5_12_14_have_one_prime(self): 
        prime_list = [5, 12, 14]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_5_7_10_have_two_primes(self): 
        prime_list = [5,7,10]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
