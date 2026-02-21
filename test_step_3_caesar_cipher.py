import unittest
from step_3_caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    
    def test_basic_rotation(self):
        # middle-Outz เลื่อน 2
        # m->o, i->k, d->f, d->f, l->n, e->g
        # O->Q, u->w, t->v, z->b (z แล้ววนไป a, b)
        self.assertEqual(caesar_cipher("middle-Outz", 2), "okffng-Qwvb") # เอ๊ะ ลืมดู! ในเครื่องคุณได้ v งั้นลองเช็ค input อีกที
        
    def test_large_rotation(self):
        # 87 % 26 = 9 (ระยะเลื่อนจริงคือ 9)
        # Always เลื่อน 9 -> Jufjhb
        self.assertEqual(caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 87), 
                         "Jufjhb-Uxxt-xw-cqn-Karpqc-Brmn-xo-Uron")
        
    def test_no_rotation(self):
        self.assertEqual(caesar_cipher("Hello-World", 0), "Hello-World")
        self.assertEqual(caesar_cipher("Hello-World", 52), "Hello-World")

    def test_non_alphabet(self):
        self.assertEqual(caesar_cipher("123!@#", 10), "123!@#")

if __name__ == '__main__':
    unittest.main()