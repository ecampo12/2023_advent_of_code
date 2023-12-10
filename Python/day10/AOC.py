import re

# def parse_input(input):
#     return input

# FML graph theory =(
def part1(grid):
    start = ()
    seen = set()
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                start = (y, x)
                break
        else:
            continue
        break
    print(start)
    seen.add(start)
    queue = [start]
    
    # doing BFS
    while queue: 
        row, col = queue.pop()
        char = grid[row][col]
        
        # Can go north/ accepts from south
        if row > 0  and char in "S|JL" and grid[row-1][col] in "|7F" and (row-1, col) not in seen:
            queue.append((row-1, col))
            seen.add((row-1, col))
        # Can go south / accepts from north
        if row < len(grid)-1 and char in "S|7F" and grid[row+1][col] in "|JL" and (row+1, col) not in seen:
            queue.append((row+1, col))
            seen.add((row+1, col))
        # Can go weast / accepts from east
        if col > 0 and char in "S-J7" and grid[row][col-1] in "-LF" and (row, col-1) not in seen:
            queue.append((row, col-1))
            seen.add((row, col-1))
        # Can go east / accepts from weast
        if col < len(grid [row])-1 and char in "S-LF" and grid[row][col+1] in "-J7" and (row, col+1) not in seen:
            queue.append((row, col+1))
            seen.add((row, col+1))
    # pipes from a loop, furthest point from start should be half of the loop
    return int(len(seen) / 2)

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input)
    # part2_sum = 0
    print(f"Part 1: {part1_sum}")
    # print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()