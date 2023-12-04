import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        expected = 4361
        sum = part1(input)
        self.assertEqual(sum, expected)
        

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        expected = 467835
        sum = part2(input)
        self.assertEqual(sum, expected)
        
if __name__ == "__main__":
    unittest.main()
    
