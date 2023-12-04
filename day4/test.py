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
        

    # def test_part2(self):
        # file = open("test_input.txt", "r")
        # input = file.read().splitlines()
        # file.close()
        # expected = 467835
        # sum = part2(input)
        # self.assertEqual(sum, expected)
        
if __name__ == "__main__":
    unittest.main()
    
