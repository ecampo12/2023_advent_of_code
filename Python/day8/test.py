import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        instructions, routes = parse_input(input)
        total = part1(instructions, routes)
        self.assertEqual(total, 2)
        
    def test_part1_example2(self):
        file = open("test_input2.txt", "r")
        input = file.read().splitlines()
        file.close()
        instructions, routes = parse_input(input)
        total = part1(instructions, routes)
        self.assertEqual(total, 6)

    # def test_part2(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read().splitlines()
    #     file.close()
    #     expected  = open("test_expected.txt", "r").read().splitlines()
    #     self.assertTrue(False)
        
if __name__ == "__main__":
    unittest.main()
    
