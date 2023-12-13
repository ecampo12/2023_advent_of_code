import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        x = parse_input(input)
        y = part1(x)
        self.assertEqual(y, 405)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        x = parse_input(input)
        y = part2(x)
        self.assertEqual(y, 400)
        
if __name__ == "__main__":
    unittest.main()
    
