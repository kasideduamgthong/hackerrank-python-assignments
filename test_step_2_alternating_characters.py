import unittest
from step_2_alternating_characters import alternating_characters

class TestAlternatingCharacters(unittest.TestCase):
    
    def test_all_same_characters(self):
        # กรณี AAAA ต้องลบ 3 ตัวเพื่อให้เหลือ A ตัวเดียว
        self.assertEqual(alternating_characters("AAAA"), 3)
        
    def test_already_alternating(self):
        # กรณี ABABAB ไม่ต้องลบเลย
        self.assertEqual(alternating_characters("ABABAB"), 0)
        
    def test_mixed_duplicates(self):
        # กรณี AAABBB ลบ A ออก 2 ลบ B ออก 2 รวมเป็น 4
        self.assertEqual(alternating_characters("AAABBB"), 4)

    def test_empty_or_single_char(self):
        # กรณีสตริงสั้นมาก
        self.assertEqual(alternating_characters("A"), 0)
        self.assertEqual(alternating_characters(""), 0)

if __name__ == '__main__':
    unittest.main()