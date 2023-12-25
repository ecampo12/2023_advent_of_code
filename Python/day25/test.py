import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        x = parse_input(input)
        self.assertEqual(part1(x), 54)

if __name__ == "__main__":
    unittest.main()
    
