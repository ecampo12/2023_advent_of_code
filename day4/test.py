import unittest
from AOC import *

class Test(unittest.TestCase):
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        expected_nums = [
            [48, 83, 17, 86],
            [32, 61],
            [1, 21],
            [84],
            [],
            []
        ]
        expected_total = [8, 2, 2, 1, 0, 0]
        sum = 0
        for i in range(len(input)):
            nums, total = part1(input[i])
            self.assertEqual(nums.sort(), expected_nums[i].sort())
            self.assertEqual(total, expected_total[i])
            sum += total
        self.assertEqual(sum, 13)
        

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read().splitlines()
        file.close()
        expected_card_count = { # Games key off by -1, to make my life easier
            0 : 1,
            1 : 2,
            2 : 4,
            3 : 8,
            4 : 14,
            5 : 1,
        }
        sum = 0
        cards = part2(input)
        for key in cards:
            self.assertEqual(cards[key], expected_card_count[key])
            sum += cards[key]
        self.assertEqual(sum, 30)
        
if __name__ == "__main__":
    unittest.main()
    
