import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        inst = parse_input(input)
        x = part1(inst)
        self.assertEqual(x, 62)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        inst = parse_input(input)
        x = part2(inst)
        self.assertEqual(x, 952408144115)
        
if __name__ == "__main__":
    unittest.main()
    
