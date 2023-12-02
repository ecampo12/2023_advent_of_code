#!/bin/bash

# function that explains the usage of the script
usage() {
    echo "Usage: $0 <number>"
    exit 1
}

if [ "$1" -eq "$1" ] 2>/dev/null; then
    mkdir day$1
    cd day$1
    touch AOCd$1.py
    echo "import unittest
from AOCd$1 import *

class Test(unittest.TestCase):
    def test_part1(self):
        input = []
        expected = []
        self.asertTrue(False)

    def test_part2(self):
        input = []
        expected  = []
        self.asertTrue(False)
        
if __name__ == \"__main__\":
    unittest.main()
    " > test.py
    commit to git
    git add .
    git commit -m "Script created: Day $1"
else
    usage
fi