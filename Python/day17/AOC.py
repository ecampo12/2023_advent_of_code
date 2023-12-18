from collections import deque
import time

class Path:
    def __init__(self, cords, direction, steps):
        self.cords = cords
        self.direction = direction
        self.steps = steps
    
    def __str__(self) -> str:
        return f"Path({self.cords}, {self.direction}, {self.steps})"
    
    def __eq__(self, o: object) -> bool:
        return self.cords == o.cords and self.direction == o.direction and self.steps == o.steps
    
    def __hash__(self) -> int:
        return hash((self.cords, self.direction, self.steps))
    
# Implementing Dial's algorithm. It's like Dijsktra's but with buckets.
# TL;DR: Because we know the are below 10, we can use buckets from 1 to 9.
# https://www.codingninjas.com/studio/library/dials-algorithm
def part1(input: [str], part2: bool = False) -> int: # learn type annotations are a thing, and they are very useful
    grid = [list(map(int, line)) for line in input]
    a = Path((0, 0), (0, 1), 0) # going right
    b = Path((0, 0), (1, 0), 0) # going down
    
    buckets = deque([[(0, a), (0, b)], *[[] for _ in range(8)]])
    seen = {a: 0, b: 0}
    goal = (len(grid) - 1, len(grid[0]) - 1)

    while buckets:
        buckets.append([])
        for heat_lost, path in buckets.popleft():
            path.steps = path.steps
            
            if path.cords == goal:
                if not part2:
                    return heat_lost
                if part2 and path.steps >= 4:
                    return heat_lost
    
            if heat_lost < seen[path]:
                continue
            
            directions = []
            dir = path.direction
            
            if part2:
                if path.steps < 10:
                    directions.append(dir)
                if path.steps >= 4:
                    directions.append((-dir[1], dir[0]))
                    directions.append((dir[1], -dir[0]))
            else:
                if path.steps < 3:
                    directions.append(dir)
                directions.append((-dir[1], dir[0]))
                directions.append((dir[1], -dir[0]))
            
            for new_dir in directions:
                row = path.cords[0] + new_dir[0]
                col = path.cords[1] + new_dir[1]
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                    new_heat_lost = heat_lost + grid[row][col]
                    new_steps = path.steps + 1 if new_dir == path.direction else 1
                    key = Path((row, col), new_dir, new_steps)
                    if key not in seen or new_heat_lost < seen[key]:
                        seen[key] = new_heat_lost
                        buckets[grid[row][col] - 1].append((new_heat_lost, key))

def part2(input: [str]):
    return part1(input, True)

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input)
    print(f"Part 1: {part1_sum}")
    
    t1 = time.perf_counter()
    part2_sum = part2(input)
    print(f"Part 2: {part2_sum}")
    print(f"Took part2: {time.perf_counter() - t1} seconds")

if __name__ == "__main__":
    main()