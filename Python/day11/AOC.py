import re
from itertools import combinations

# Goes through input 3 times, but F it. It's fast enough.
def parse_input(input):
    galaxy = {}
    empty_row = []
    empty_col = []
    count = 1
    for y, row in enumerate(input):
        for x, col in enumerate(row):
            if col == "#":
                galaxy[count] = (y, x)
                count += 1
    for i, row in enumerate(input):
        if all(col == "." for col in row):
            empty_row.append(i)
    for i, col in enumerate(zip(*input)): # Trick to interate over columns
        if all(col == "." for col in col):
            empty_col.append(i)
    return galaxy, empty_row, empty_col

# Middle shcool math, baby!
def distance(start, end, empty_rows, empty_cols, expand=2):
    manhattan_dist = abs(start[0] - end[0]) + abs(start[1] - end[1])

    # Additional distance for crossing empty rows and columns
    row_crossings = (expand - 1)*len([row for row in empty_rows if min(start[0], end[0]) < row < max(start[0], end[0])])
    col_crossings = (expand - 1)*len([col for col in empty_cols if min(start[1], end[1]) < col < max(start[1], end[1])])

    return manhattan_dist + row_crossings + col_crossings

def find_all_galaxy_pairs(galaxy_map):
    galaxy_ids = list(galaxy_map.keys())
    galaxy_pairs = list(combinations(galaxy_ids, 2))
    result = [((id1, galaxy_map[id1]), (id2, galaxy_map[id2])) for (id1, id2) in galaxy_pairs]
    return result


def part1(galaxy, empty_rows, empty_cols):
    dists = []
    combos = find_all_galaxy_pairs(galaxy)    
    for combo in combos:
        start = combo[0][1]
        end = combo[1][1]
        dist = distance(start, end, empty_rows, empty_cols)
        dists.append(dist)
    
    return sum(dists)

def part2(galaxy, empty_rows, empty_cols, expand=1):
    dists = []
    combos = find_all_galaxy_pairs(galaxy)    
    for combo in combos:
        start = combo[0][1]
        end = combo[1][1]
        dist = distance(start, end, empty_rows, empty_cols, expand)
        dists.append(dist)
    
    return sum(dists)

def main():
    input = open("input.txt", "r").read().splitlines()
    galaxies, rows, cols = parse_input(input)
    part1_sum = part1(galaxies, rows, cols)
    part2_sum = part2(galaxies, rows, cols, 1000000)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()