import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        total = part1(input)
        self.assertEqual(total, 32000000)

    def test_part1_2(self):
        file = open("test_input2.txt", "r")
        input = file.read().splitlines()
        file.close()
        total = part1(input)
        self.assertEqual(total, 11687500)
        
if __name__ == "__main__":
    unittest.main()
    
