import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        x = part1(input)
        self.assertEqual(x, 21)

    # def test_part2(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read().splitlines()
    #     file.close()
    #     x = part2(input)
    #     self.assertEqual(x, 525152)
        
if __name__ == "__main__":
    unittest.main()
    
