import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        b =  parse_input(input)
        x = part1(b)
        self.assertEqual(x, 5)

    # def test_part2(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read().splitlines()
    #     file.close()
    #     expected  = open("test_expected.txt", "r").read().splitlines()
    #     self.assertTrue(False)
        
if __name__ == "__main__":
    unittest.main()
    
