import unittest
from AOC import *

class Test(unittest.TestCase):
    # def test_part1(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read().splitlines()[0].split(",")
    #     file.close()
    #     x = part1(input)
    #     self.assertEqual(x, 1320)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()[0].split(",")
        file.close()
        x = part2(input)
        self.assertTrue(x, 145)
        
if __name__ == "__main__":
    unittest.main()
    
