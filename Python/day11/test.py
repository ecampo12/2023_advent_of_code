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

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        
        galaxies, rows, cols = parse_input(input)
        dist_sum10 = part2(galaxies, rows, cols, 10)
        self.assertEqual(dist_sum10, 1030)
        
        dist_sum100 = part2(galaxies, rows, cols, 100)
        self.assertEqual(dist_sum100, 8410)
        
if __name__ == "__main__":
    unittest.main()
    
