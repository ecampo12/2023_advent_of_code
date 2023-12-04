import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        expected = 4361
        sum = part1(input)
        self.assertEqual(sum, expected)
        

    # def test_part2(self):
    #     input = open("test_input.txt", "r").read().splitlines()
    #     expected  = open("test_expected.txt", "r").read().splitlines()
    #     self.assertTrue(False)
        
if __name__ == "__main__":
    unittest.main()
    
