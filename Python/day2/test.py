import unittest
from AOCd2 import *

class Test(unittest.TestCase):
    def test_part1(self):
        input = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
        expected = [True, True, False, False, True]
        sum = 0
        for i in range(len(input)):
            valid = part1(input[i])
            self.assertEqual(valid, expected[i])
            if valid:
                sum += i + 1
        self.assertEqual(sum, 8)
        

    def test_part2(self):
        input = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
        expected  = [48, 12, 1560, 630, 36]
        sum = 0
        for i in range(len(input)):
            power = part2(input[i])
            self.assertEqual(power, expected[i])
            sum += power
        self.assertEqual(sum, 2286)
        
        
if __name__ == "__main__":
    unittest.main()
    
