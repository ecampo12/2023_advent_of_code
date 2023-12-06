import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        times, distances = parse_input(input)
        x = part1(times, distances)
        self.assertEqual(x, 288)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        times, distances = parse_input(input)
        x = part2(times, distances)
        self.assertEqual(x, 71503)
        
if __name__ == "__main__":
    unittest.main()
    
