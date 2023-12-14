def tiltNorth(input):
    transposed = list(map("".join, zip(*input)))
    new_grid = []
    for row in transposed:
        sorted_row = []
        for group in row.split('#'):
            sorted_row.append("".join(sorted(list(group), reverse=True)))
        new_grid.append("#".join(sorted_row))
    new_grid = list(map("".join, zip(*new_grid)))
    return new_grid

# Like tiltNorth, we transpose the grid, but instead of tarnsposing back we rotate the grid 90 degrees left and "tiltNorth" 4 times
#      N                         W                                      W
#   |a b c|    Transpose      |g d a|    Tilt    |g d a|  Reverse    |a d g|   Repeat 3 more times
# W |d e f| E  ===========> S |h e b| N  =====>  |h e b|  =======> N |b e h| S =====>  
#   |g h i|                   |i f c|            |i f c|             |c f i|
#      S                         E                                      E
def tilt_cyclic(grid):
    for _ in range(4):
        transposed = tuple(map("".join, zip(*grid)))
        new_grid = []
        for row in transposed:
            sorted_row = []
            for group in row.split('#'):
                sorted_row.append("".join(sorted(tuple(group), reverse=True)))

            final_row_string = "#".join(sorted_row)
            new_grid.append(final_row_string)

        new_grid = tuple(new_grid)
        grid = tuple(row[::-1] for row in new_grid)
    return grid
    
def part1(input):
    grid = tiltNorth(input)
    sum = 0
    for i, row in enumerate(grid):
        rocks = len([x for x in row if x=='O'])
        sum += (len(grid) - i) * rocks
    return sum


def part2(input):
    grid = tuple(input)
    seen = {grid}
    existing_grids = [grid]
    count = 0
    
    while True:
        count += 1
        grid = tilt_cyclic(grid)
        if grid in seen:
            break
        seen.add(grid)
        existing_grids.append(grid)
    first_appearance = existing_grids.index(grid)
    # The grid will repeat every (count - first_appearance) iterations
    grid = existing_grids[(1000000000 - first_appearance) % (count - first_appearance) + first_appearance]
    
    sum = 0
    for i, row in enumerate(grid):
        rocks = len([x for x in row if x=='O'])
        sum += (len(grid) - i) * rocks
    return sum

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input)
    part2_sum = part2(input)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()