import unittest
from AOC import *

class Test(unittest.TestCase):        
    def test_part1(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        expected = [
             [79, 81, 81, 81, 74, 78, 78, 82],
             [14, 14, 53, 49, 42, 42, 43, 43],
             [55, 57, 57, 53, 46, 82, 82, 86],
             [13, 13, 52, 41, 34, 34, 35, 35]
        ]
        locations, paths = part1(input)
        for i in range(len(expected)):
            self.assertListEqual(expected[i], paths[i])
            self.assertEqual(expected[i][-1], locations[i])
        self.assertEqual(min(locations), 35)

    def test_part2(self):
        file = open("test_input.txt", "r")
        input = file.read()
        file.close()
        locations = part2(input)
        self.assertEqual(min(locations)[0], 46)
        
if __name__ == "__main__":
    unittest.main()
    
