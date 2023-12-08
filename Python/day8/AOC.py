import re

def parse_input(input):
    instructions = [0 if c == 'L' else 1 for c in input[0]]
    routes = {}
    for i in range(2, len(input)):
        x = re.findall(r"\w+", input[i])
        routes[x[0]] = (x[1], x[2])
    
    return instructions, routes

def part1(instructions, routes):
    curr_inst = instructions[0]
    curr_loc = 'AAA'
    count = 1
    while curr_loc != 'ZZZ':
        curr_loc = routes[curr_loc][curr_inst]
        curr_inst = instructions[count%len(instructions)]
        count += 1
        print(f"{curr_loc} {curr_inst}")
    return count - 1

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read().splitlines()
    instructions, routes = parse_input(input)
    part1_count = part1(instructions, routes)
    part2_sum = 0
    print(f"Part 1: {part1_count}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()