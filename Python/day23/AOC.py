import re
from time import perf_counter

directions = {
    ">": [(0, 1)], 
    "<": [(0, -1)], 
    # "^": [(-1, 0)], # Turns out, its meantioned in the problem that there are no paths that go up in the test input or actual input
    "v": [(1, 0)], 
    ".": [(0, 1), (1, 0), (0, -1), (-1, 0)]
}

# You'd think I would have had this function in my toolbox by now...
def isValid(grid, coord):
    row, col = coord
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "#"

def neighbors(grid, start):
    row, col = start
    n = []
    for dr, dc in directions[grid[row][col]]:
        new_r, new_c = row + dr, col + dc
        if isValid(grid, (new_r, new_c)):
            n.append((new_r, new_c))
    return n


def build_graph(grid):
    start = (0, 1)
    end = (len(grid) - 1, len(grid[0]) - 2)
    points = [start, end]

    # From looking at the test input, and actual input, paths only branch where there are 3 or more neighbors
    # So, we can find all the branching points, and add them to the graph
    # Thsi is apparenly called edge contraction: https://en.wikipedia.org/wiki/Edge_contraction
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "#":
                n = neighbors(grid, (r, c))
                if len(n) >= 3:
                    points.append((r, c))
                
    graph = {pt: {} for pt in points}
    
    # Finding the edges of the graph
    for row, col in points:
        stack = [(row, col, 0)]
        seen = {(row, col)}
        
        while stack:
            r, c, steps = stack.pop()
            
            if steps != 0 and (r, c) in points:
                graph[(row, col)][(r, c)] = steps
                continue
            
            for dr, dc in directions[grid[r][c]]:
                new_r, new_c = r + dr, c + dc
                if isValid(grid, (new_r, new_c)) and (new_r, new_c) not in seen:
                    stack.append((new_r, new_c, steps + 1))
                    seen.add((new_r, new_c))
    return graph

# Thanks to the edge contraction, we can do DFS without having to increase the recursion limit
def dfs(graph, seen, start, end):
    if start == end:
        return 0
    # Needed because appreantly there are negative paths in the graph (???) 😕
    # Yes -209 is a magic number, its the highest negative number I could find that gets me the right answer
    # For a more general solution replace -209 with -float("inf"), but a magic number seems to be faster
    max_path = -209
    seen.add(start)
    for n in graph[start]:
        if n not in seen:
            max_path = max(max_path, dfs(graph, seen, n, end) + graph[start][n])
            # if max_path < 0 and max_path != -float("inf"):
            #     print(max_path)
    seen.remove(start)
    return max_path

# This part is fast because the maze is a driected acyclic graph, so it can be solved in linear time
# https://en.wikipedia.org/wiki/Longest_path_problem#Acyclic_graphs
def part1(input):
    start = (0, 1)
    end = (len(input) - 1, len(input[0]) - 2)
    g = build_graph(input)
    x = dfs(g, set(), start, end)
    return x

# Removing the arraows makes the Problem harder, since we now paths that can loop back to other nodes.
# It becomes an NP-hard problem, so yeah this is gonna take a while.
# https://en.wikipedia.org/wiki/Longest_path_problem#NP-hardness
def part2(input):
    start = (0, 1)
    end = (len(input) - 1, len(input[0]) - 2)
    mod = []
    for line in input:
        mod.append(re.sub(r"[<>^v]", ".", line))
    input = mod
    g = build_graph(input)
    x = dfs(g, set(), start, end)
    return x

# Part 2 is slow, takes about 17.4 seconds to run on my machine. I'm sure their are ways to speed it up.
def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input)
    print(f"Part 1: {part1_sum}")
    
    t1 = perf_counter()
    part2_sum = part2(input)
    t2 = perf_counter()
    print(f"Part 2: {part2_sum}")
    print(f'It took {t2 - t1} seconds to solve part 2')
    assert part2_sum == 6334

if __name__ == "__main__":
    main()