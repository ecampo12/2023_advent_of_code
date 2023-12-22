import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        b =  parse_input(input)
        x = part1(b)
        self.assertEqual(x, 5)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        b = parse_input(input)
        x = part2(b)
        self.assertEqual(x, 7)
        
if __name__ == "__main__":
    unittest.main()
    
