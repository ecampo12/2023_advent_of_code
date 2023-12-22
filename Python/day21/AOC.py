from collections import deque
from freq import bfs

# Just a simple BFS, but we need to keep track of the number of steps we've taken
def part1(grid, steps):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start = (r, c)
                break
    final = set()
    visited = {start}
    # Learned my lesson from 20, using a deque instead of a list
    queue = deque([(start[0], start[1], steps)])

    while queue:
        row, col, curr_step = queue.popleft()

        if curr_step % 2 == 0: # Even steps means we can we can backtrack to this spot multiple times
            final.add((row, col))
        if curr_step == 0:
            continue
        
        #              left,    right,  up,     down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc
            if 0 > new_r >= len(grid) or 0 > new_c >= len(grid[0]):
                continue
            if grid[new_r][new_c] == "#" or (new_r, new_c) in visited:
                continue
            visited.add((new_r, new_c))
            queue.append((new_r, new_c, curr_step - 1))
    return len(final)

# Yeah, just read freq.py for the details on this one
def part2(grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start = (r, c)
                break
    hieght = len(grid)
    mod = 26_501_365 % hieght       # Yes, I hard coded the input
    steps = (26501365 - 65) // 131  # Too tired to explain where the numbers come from, just read freq.py
    f0, f1, f2 = bfs(grid, start, [mod, mod + hieght, mod + 2*hieght])
    c = f0
    a = (f2 - 2*f1 + f0) // 2
    b = f1 - f0 - a
    # The formula for the sequence
    f = lambda n: a*n**2 + b*n + c
    return f(steps)

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input, 64)
    part2_sum = part2(input)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()