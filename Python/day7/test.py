import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        hands, bids = parse_input(input)
        part1_total = part1(hands, bids)
        self.assertEqual(part1_total, 6440)
        

    # def test_part2(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read()
    #     file.close()
    #     self.assertTrue(False)
        
if __name__ == "__main__":
    unittest.main()
    
