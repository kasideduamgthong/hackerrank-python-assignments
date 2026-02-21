import unittest
from step_5_grid_challenge import grid_challenge

class TestGridChallenge(unittest.TestCase):
    
    def test_valid_grid(self):
        # กรณีที่เรียงแถวแล้ว คอลัมน์ก็เรียงด้วย
        grid = ['abc', 'hjk', 'mpq']
        self.assertEqual(grid_challenge(grid), "YES")
        
    def test_invalid_grid(self):
        # กรณีที่เรียงแถวแล้ว แต่คอลัมน์ (แนวตั้ง) ไม่เรียง
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        # แถวแรกเรียงเป็น 'abcde' แถวสอง 'fghij' 
        # ต้องเช็คว่า 'a' < 'f' จริงไหมไปเรื่อยๆ
        self.assertEqual(grid_challenge(grid), "NO")
        
    def test_single_element(self):
        # เคสขอบเขต: ตารางขนาด 1x1
        grid = ['z']
        self.assertEqual(grid_challenge(grid), "YES")

    def test_all_same_characters(self):
        # เคสตัวอักษรเหมือนกันหมด
        grid = ['aaa', 'aaa', 'aaa']
        self.assertEqual(grid_challenge(grid), "YES")

if __name__ == '__main__':
    unittest.main()