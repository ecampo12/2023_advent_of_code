import unittest
from AOC import *

class Test(unittest.TestCase):
    # def test_parse_input(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read()
    #     file.close()
    #     test_seeds = [79, 14, 55, 13]
    #     test_soil = [81, 14, 57, 13]
    #     seeds, map = parse_input(input)
    #     seed_to_soil = map["seed-to-soil map:"]

    #     for i in range(len(test_seeds)):
    #         self.assertTrue(test_seeds[i] in seeds)
    #         if test_seeds[i] == 14 or test_seeds[i] == 13:
    #             with self.assertRaises(KeyError):
    #                 seed_to_soil[test_seeds[i]]
    #         else:
    #             self.assertEqual(test_soil[i], seed_to_soil[test_seeds[i]])
        
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
        # parse_input(input)
        locations, paths = part1(input)
        for i in range(len(expected)):
            self.assertListEqual(expected[i], paths[i])
            self.assertEqual(expected[i][-1], locations[i])
        # print(min(locations))
        self.assertEqual(min(locations), 35)

    # def test_part2(self):
    #     file = open("test_input.txt", "r")
    #     input = file.read().splitlines()
    #     file.close()
    #     expected  = open("test_expected.txt", "r").read().splitlines()
    #     self.assertTrue(False)
        
if __name__ == "__main__":
    unittest.main()
    
