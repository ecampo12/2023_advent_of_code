#!/bin/bash

usage() {
    echo "Usage: $0 <number>"
    exit 1
}

if [ "$1" -eq "$1" ] 2>/dev/null; then
    mkdir day$1
    cp AOC_temp.py day$1/AOC.py
    cp test_temp.py day$1/test.py
    cd day$1
    touch "test_input.txt"
    touch "test_expected.txt"
    commit to git
    git add .
    git commit -m "Script created: Day $1"
else
    usage
fi