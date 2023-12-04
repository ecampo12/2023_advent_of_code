import re

def parse_input(input):
    numbers = {}
    symbols = {}
    for i in range(len(input)):
        num_matches = re.finditer(r"(\d+)", input[i])
        sym_matches = re.finditer(r"([^\d|^.])", input[i])
        if num_matches != []:
            numbers[i] = [x for x in num_matches]
        if sym_matches != []:
            symbols[i] = [x for x in sym_matches]
    return numbers, symbols
        
def get_adjacent(numbers, sym_pos, key):
    #(y, x)
    # (-1, -1) (-1, 0) (-1, 1)
    # (0, -1)  (y, x)  (0, 1)
    # (1, -1)  (1, 0)  (1, 1)
    positions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1,-1), (-1, 0)]
    seen, adjacent = [], []
    for pos in positions:
        y = key + pos[0]
        x = sym_pos + pos[1]
        if y in numbers.keys():
            for num in numbers[y]:
                if num.span()[0] <= x and num.span()[1] > x and (y, num.span()) not in seen:
                    adjacent.append(num.group())
                    seen.append((y, num.span()))
    return adjacent
    
def part1(input):
    part_sum = 0
    numbers, symbols = parse_input(input)
    for key, symbol in symbols.items():
        for i in range(len(symbol)):
            adj = get_adjacent(numbers, symbol[i].span()[0], key)
            for a in adj:
                part_sum += int(a)
    return part_sum

def part2(input):
    part_sum = 0
    numbers, symbols = parse_input(input)
    for key, symbol in symbols.items():
        for i in range(len(symbol)):
            if symbol[i].group() == "*":
                adj = get_adjacent(numbers, symbol[i].span()[0], key)
                if len(adj) == 2:
                    part_sum += int(adj[0]) * int(adj[1])
                
    return part_sum

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input) 
    part2_sum = part2(input)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()