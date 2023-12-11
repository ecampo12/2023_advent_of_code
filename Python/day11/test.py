import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        galaxies, rows, cols = parse_input(input)
        dist_sum = part1(galaxies, rows, cols)
        self.assertEqual(dist_sum, 374)

    # def test_part2(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read().splitlines()
    #     file.close()
    #     expected  = open("test_expected.txt", "r").read().splitlines()
    #     self.assertTrue(False)
        
if __name__ == "__main__":
    unittest.main()
    
