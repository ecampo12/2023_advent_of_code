import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        w, p = parse_input(input)
        sum = part1(w, p)
        self.assertEqual(sum, 19114)
        
    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        w, _ = parse_input(input)
        total = part2(w)
        self.assertEqual(total, 167409079868000)
        
if __name__ == "__main__":
    unittest.main()
    
