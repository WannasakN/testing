from code.Caesar_Cipher import caesarCipher

import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_Helloworld_in_caesarcipher(self): #เทสใส่ตัวอักษรพิเศษ
        x = 'Hello, world!'
        result = caesarCipher(x,3)
        self.assertEqual(result,'Khoor, zruog!')
    def test_Thequickbrownfoxjumpsoverthelazydog_in2_caesarcipher(self): #เทสใส่ช่องว่างระหว่างคำ
        x = 'The quick brown fox jumps over the lazy dog'
        result = caesarCipher(x,7)
        self.assertEqual(result,'Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn')
    def test_abcXYZ123_in_caesarcipher(self): #เทสใส่ตัวเลข
        x = 'abcXYZ123'
        result = caesarCipher(x,10)
        self.assertEqual(result,'klmHIJ123')
    def test_A5Rroymak_in_caesarcipher(self): #เทสใส่ค่า k = 0
        x = 'A5Rroymak'
        result = caesarCipher(x,0)
        self.assertEqual(result,'A5Rroymak')
    def test_Empty_string_in_caesarcipher(self): #เทสไม่ใส่ค่าอะไรเลย
        x = ''
        result = caesarCipher(x,5)
        self.assertEqual(result,'')
