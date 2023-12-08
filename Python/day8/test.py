import unittest
from AOC import *

class Test(unittest.TestCase):
    # def test_part1(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read().splitlines()
    #     file.close()
    #     instructions, routes, _ = parse_input(input)
    #     total = part1(instructions, routes)
    #     self.assertEqual(total, 2)
        
    # def test_part1_example2(self):
    #     file = open("test_input2.txt", "r")
    #     input = file.read().splitlines()
    #     file.close()
    #     instructions, routes, _ = parse_input(input)
    #     total = part1(instructions, routes)
    #     self.assertEqual(total, 6)

    def test_part2(self):
        file = open("test_input3.txt", "r")
        input = file.read().splitlines()
        file.close()
        instructions, routes, starters = parse_input(input)
        total = part2(instructions, routes, starters)
        self.assertEqual(total, 6)
        
if __name__ == "__main__":
    unittest.main()
    
