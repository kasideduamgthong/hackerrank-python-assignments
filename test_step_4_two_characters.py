import unittest
from step_4_two_characters import two_characters

class TestTwoCharacters(unittest.TestCase):
    
    def test_sample_case(self):
        # beabeefeab -> babab (length 5)
        self.assertEqual(two_characters("beabeefeab"), 5)
        
    def test_no_valid_string(self):
        # aabb -> aabb (not alternating)
        self.assertEqual(two_characters("aabb"), 0)
        
    def test_single_character(self):
        self.assertEqual(two_characters("aaaaa"), 0)

    def test_already_alternating(self):
        self.assertEqual(two_characters("ababab"), 6)

if __name__ == '__main__':
    unittest.main()