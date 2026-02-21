import unittest
from step_5_grid_challenge import grid_challenge

class TestGridChallenge(unittest.TestCase):
    
    def test_valid_grid(self):
        # กรณีที่เรียงแถวแล้ว คอลัมน์ก็เรียงด้วย
        grid = ['abc', 'hjk', 'mpq']
        self.assertEqual(grid_challenge(grid), "YES")
        
    def test_invalid_grid(self):
        # ตารางนี้เมื่อเรียงแถวแล้ว จะได้:
        # ['abc']
        # ['abd']
        # ['aac']  <-- แถวนี้แหละที่จะทำให้คอลัมน์ที่ 3 (c) พัง เพราะ 'd' > 'c'
        grid = ['cba', 'dab', 'aca']
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