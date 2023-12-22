
from collections import deque

# had rewrite the bfs, there is a bug the original bfs that I couldn't find. Rewriting it fixed it. ???
def bfs(grid, start, steps):
    x, y = start
    visited = {(x, y): 0}
    dist = 0
    q = deque()
    q.append((x, y))
    result = []
    while dist < max(steps):
        dist += 1
        q2 = deque()
        while q:
            x, y = q.popleft()    
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = dx + x, dy + y
                tx, ty = nx % len(grid[0]), ny % len(grid)
                if grid[ty][tx] != '#' and (nx, ny) not in visited:
                    visited[(nx, ny)] = dist
                    q2.append((nx, ny))
        q = q2
        # commentting out the next line will get all the distances, for debugging
        if dist in steps:
            result.append(len([x for x in visited.values() if x % 2 == dist % 2]))
    return result
    
if __name__ == "__main__":

    #  Another puzzel that requires analysis of the input data to find a pattern.

    grid = open("input.txt", "r").read().splitlines()

    # Checking size of grid
    hieght = len(grid)
    width = len(grid[0])

    # Looks like our grid is a square
    assert hieght == width

    # Checking for the start position
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start = (r, c)
                break
            
    # height and width are odd
    print(f"Grid size: {hieght}x{width}")
    print(f"Start position: {start}")

    assert start[0] * 2 + 1 == hieght
    assert start[0] * 2 + 1 == hieght
    # Start is in the center of the grid

    # Looking at the input it looks like the column and row the start is on is empty
    for i in grid[start[0]]:
        assert i == "." or i == "S"

    trans = list(zip(*grid))
    for i in trans[start[1]]:
        assert i == "." or i == "S"

    # Asumption correct: The start is on an empty row and column

    # We are asked to travel 26501365 steps
    # it takes 65 steps to get from the center to the edge, 131 steps to cross the whole grid
    squares = (26501365 - 65) // 131
    print(f"Squares: {squares}")

    # If we travel in a straight line for 26501365 steps, we would travel 202300 squares. Which is a nice easter egg!
    mod = 26_501_365 % hieght
    print(f"Mod: {mod}")
    # 26501365 % 131 = 65


    # The last few probelem were retreads of earlier problems, so one of ealier solutions can be used to solve this ???

    # Day 9 had us implement a Quadratic Sequences - Difference Method to find the next number in a sequence
    prev = 0
    diffs = []
    print("i," + "mod+h* i, x".ljust(10) +", x - prev")
    vals = []
    for i in range(5):
        x = bfs(grid, start, [mod + hieght * i])
        print(i, mod + hieght * i, x[-1], x[-1] - prev)
        diffs.append(x[-1] - prev)
        prev = x[-1]
        vals.append(x[-1])

    # get diff between diffs
    diff2 = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
    print(diff2)
    diff3 = [diff2[i+1] - diff2[i] for i in range(len(diff2)-1)]
    print(diff3)

    # Doing three iterates of the difference method, we get the solution to part1. We must be on the right track
    f0, f1, f2 = bfs(grid, start, [mod, mod + hieght, mod + 2*hieght])

    # Link below explains how to solve a quadratic sequence using the difference method, and how to find the formula for the sequence
    # It is a system of three equations, with three unknowns, so we can solve it using linear algebra
    # https://www.radfordmathematics.com/algebra/sequences-series/difference-method-sequences/quadratic-sequences.html
    c = f0
    a = (f2 - 2*f1 + f0) // 2
    b = f1 - f0 - a


    # The formula for the sequence
    f = lambda n: a*n**2 + b*n + c

    # assert
    assert f(0) == vals[0]
    assert f(1) == vals[1]
    assert f(2) == vals[2]
    assert f(3) == vals[3]
    assert f(4) == vals[4]

    # Solution to part 2 FOUND!!!
    print(f(squares))
