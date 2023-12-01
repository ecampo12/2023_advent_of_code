import unittest
from AOCd1 import *

class Test(unittest.TestCase):
    def test_part1(self):
        input = ["1abc2",
             "pqr3stu8vwx",
             "a1b2c3d4e5f",
             "treb7uchet"]
        expected = [12, 38, 15, 77]
        sum = 0
        for i in range(len(input)):
            num = part1(input[i])
            if num != expected[i]:
                print(f'{input} {num} != {expected[i]}')
            sum += num
        self.assertEqual(sum, 142)

    def test_part2(self):
        input = ["two1nine",
         "eightwothree",
         "abcone2threexyz",
         "xtwone3four",
         "4nineeightseven2",
         "zoneight234",
         "7pqrstsixteen"
    ]
        expected  = [29, 83, 13, 24, 42, 14, 76]

        sum = 0
        for i in range(len(input)):
            num = part2(input[i])
            if num != expected[i]:
                print(f'{input} {num} != {expected[i]}')
            sum += num

        self.assertEqual(sum, 281)
    
    def test_part2_overlap(self):
        input = "9eightszgdhftggrktkzbsmnhtwonekh"
        expected = 91
        self.assertEqual(part2(input), expected)
        
if __name__ == "__main__":
    unittest.main()