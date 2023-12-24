import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        x = parse_input(input)
        y = part1(x, 7, 27)
        self.assertEqual(y, 2)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        x = parse_input(input)
        y = part2(x)
        self.assertEqual(y, 47)
        
if __name__ == "__main__":
    unittest.main()
    
