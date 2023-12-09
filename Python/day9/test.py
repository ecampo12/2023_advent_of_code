import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        input = parse_input(input)
        next_nums = part1(input)        
        self.assertEqual(next_nums, 114)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        input = parse_input(input)
        next_nums = part2(input)        
        self.assertEqual(next_nums, 2)
        
if __name__ == "__main__":
    unittest.main()
    
