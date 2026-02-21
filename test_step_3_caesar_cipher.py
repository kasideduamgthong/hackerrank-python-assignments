import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    
    def test_basic_rotation(self):
        self.assertEqual(caesar_cipher("middle-Outz", 2), "okffng-Qwub") # ทดสอบการเลื่อนปกติ
        
    def test_large_rotation(self):
        self.assertEqual(caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 87),   # ทดสอบกรณี k มากกว่า 26 (เช่น 87)
                         "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")
        
    def test_no_rotation(self):
        self.assertEqual(caesar_cipher("Hello-World", 0), "Hello-World")  # ทดสอบกรณี k = 0 หรือ k เป็นทวีคูณของ 26
        self.assertEqual(caesar_cipher("Hello-World", 52), "Hello-World")

    def test_non_alphabet(self):
        self.assertEqual(caesar_cipher("123!@#", 10), "123!@#") # ทดสอบตัวเลขและสัญลักษณ์

if __name__ == '__main__':
    unittest.main()