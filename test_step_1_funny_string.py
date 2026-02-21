import unittest
from step_1_funny_string import funny_string

class TestFunnyString(unittest.TestCase):
    
    def test_is_funny(self):  # ทดสอบกรณีที่เป็น Funny (เพื่อให้ Code รันไปจนจบฟังก์ชัน)
        self.assertEqual(funny_string("acxz"), "Funny")
         
    def test_not_funny(self):  # ทดสอบกรณีที่ไม่เป็น Funny (เพื่อให้ Code เข้าเงื่อนไข if diff_s != diff_r)
        self.assertEqual(funny_string("bcxz"), "Not Funny")
        
    def test_minimal_length(self):     # ทดสอบกรณีขอบเขต: สตริงสั้นที่สุด 2 ตัว เพื่อให้ Code รันไปจนจบฟังชัน
        self.assertEqual(funny_string("ab"), "Funny")

if __name__ == '__main__':
    unittest.main()