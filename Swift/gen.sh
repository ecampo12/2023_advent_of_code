#!/bin/bash

usage() {
    echo "Usage: $0 #"
    exit 1
}

if [ $# -ne 1 ]; then
    usage
fi

day=$1

echo "day: $day"

if [ ! -d "day$day" ]; then
    mkdir "day$day"
    cd "day$day"
    swift package init --name AOC --type executable
    cd ..
    cp inputData_temp.swift "day$day/Sources/inputData.swift"
    echo "Created day$day folder"

    git add "day$day"
    git commit -m "Swift: Added day$day folder"
fi