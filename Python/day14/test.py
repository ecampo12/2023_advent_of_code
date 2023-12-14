import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        sum = part1(input)
        self.assertEqual(sum, 136)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        sum = part2(input)
        self.assertEqual(sum, 64)
        
if __name__ == "__main__":
    unittest.main()
    
