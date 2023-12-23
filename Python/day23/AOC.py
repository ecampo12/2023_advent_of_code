import re
from collections import deque
from time import perf_counter
import sys
sys.setrecursionlimit(1000000)

directions = {
    ">": [(0, 1)], 
    "<": [(0, -1)], 
    # "^": [(-1, 0)], 
    "v": [(1, 0)], 
    ".": [(0, 1), (1, 0), (0, -1), (-1, 0)]
}

def neighbors(grid, start):
    row, col = start
    n = []

    for dr, dc in directions[grid[row][col]]:
        new_r, new_c = row + dr, col + dc
        if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
            continue
        if grid[new_r][new_c] == "#":
            continue
        n.append((new_r, new_c))
    return n

def dfs(grid, start, end, path, pathset, max_path):
    if start == end:
        max_path = max(max_path, len(path))
    for n in neighbors(grid, start):
        if n not in pathset:
            path.append(n)
            pathset.add(n)
            max_path = max(max_path, dfs(grid, n, end, path, pathset, max_path))
            pathset.remove(n)
            path.pop(-1)
    return max_path

def part1(input):
    start = (0, 1)
    end = (len(input) - 1, len(input[0]) - 2)
 
    max_path = dfs(input, start, end, [], set(), 0)
    return max_path

def part2(input):
    start = (0, 1)
    end = (len(input) - 1, len(input[0]) - 2)
    for line in input:
        line = re.sub(r"[<>^v]", ".", line)
        # print(line)
    # x = dfs(input, start, end, seen, 0)
    max_path = dfs(input, start, end, [], set(), 0)
    print(max_path)
    return max_path

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input)
    t1 = perf_counter()
    print(f"Part 1: {part1_sum}")
    t2 = perf_counter()
    print(f'It took {t2 - t1} seconds to solve part 1')
    
    part2_sum = part2(input)
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()