import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        # rocks, start = parse_input(input)
        # x = find_steps(input, rocks, start, 6)
        x = part1(input, 6)
        self.assertEqual(x, 16)

    # def test_part2(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read().splitlines()
    #     file.close()
    #     self.assertTrue(False)
        
if __name__ == "__main__":
    unittest.main()
    
