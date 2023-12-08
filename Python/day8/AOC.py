import re
from functools import reduce 
from math import lcm

def parse_input(input):
    instructions = [0 if c == 'L' else 1 for c in input[0]]
    routes = {}
    start_nodes = []
    for i in range(2, len(input)):
        x = re.findall(r"\w+", input[i])
        routes[x[0]] = (x[1], x[2])
        if x[0].endswith('A'):
            start_nodes.append(x[0])
    return instructions, routes, start_nodes

def part1(instructions, routes):
    curr_inst = instructions[0]
    curr_loc = 'AAA'
    count = 1
    while curr_loc != 'ZZZ':
        curr_loc = routes[curr_loc][curr_inst]
        curr_inst = instructions[count%len(instructions)]
        count += 1
    return count - 1

# Each node will cycle back to itself after a certain number of steps (check freq.py for details)
# need to find the LCM of all of these cycles
def part2(instructions, routes, start_nodes):
    curr_inst = instructions[0]
    counts = []
    for node in start_nodes:
        curr_loc = node
        count = 1
        while True:
            curr_loc = routes[curr_loc][curr_inst]
            curr_inst = instructions[count%len(instructions)]
            count += 1
            if curr_loc.endswith('Z'):
                break
        counts.append(count-1)
    return lcm(*counts)

def main():
    input = open("input.txt", "r").read().splitlines()
    instructions, routes, starters = parse_input(input)
    part1_count = part1(instructions, routes)
    part2_sum = part2(instructions, routes, starters)
    print(f"Part 1: {part1_count}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()