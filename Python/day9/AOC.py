import re

def parse_input(input):
    return [list(map(int, line.split(" "))) for line in input] 

def getNextNumber(input):
    if all(x == 0 for x in input):
        return 0
    diff = [input[i+1] - input[i] for i in range(len(input)-1)]
    return input[-1] + getNextNumber(diff)

def getPrevNumber(input):
    if all(x == 0 for x in input):
        return 0
    diff = [input[i+1] - input[i] for i in range(len(input)-1)]
    return input[0] - getPrevNumber(diff)

def part1(input):
    next_nums = []
    for line in input:
        x = getNextNumber(line)
        next_nums.append(x)
    return sum(next_nums)

def part2(input):
    prev_nums = []
    for line in input:
        x = getPrevNumber(line)
        prev_nums.append(x)
    return sum(prev_nums)

def main():
    input = open("input.txt", "r").read().splitlines()
    nums = parse_input(input)
    part1_sum = part1(nums)
    part2_sum = part2(nums)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()