import re

def parse_input(input):
    print(len(input))
    rocks = {}
    count = len(input)
    for line in input:
        rocks[count] = len([x for x in line if x=='O'])
        # print(rocks[count])
        count -= 1
    print(rocks)
    return rocks

def tiltNorth(input):
    transposed = list(map("".join, zip(*input)))
    new_grid = []
    for row in transposed:
        sorted_row = []
        for group in row.split('#'):
            sorted_row.append("".join(sorted(list(group), reverse=True))) # Sorting the cols moves the rocks up
    new_grid = list(map("".join, zip(*new_grid)))
    return new_grid

def part1(input):
    grid = tiltNorth(input)
    for row in grid:
        print(row)
    sum = 0
    for i, row in enumerate(grid):
        rocks = len([x for x in row if x=='O'])
        sum += (len(grid) - i) * rocks
        print(f"{i}: {rocks} * {len(grid) - i} = {(len(grid) - i) * rocks}")
    return sum

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input)
    part2_sum = 0
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()