from dataclasses import dataclass, field
from collections import deque
from time import process_time

@dataclass(order=True, unsafe_hash=True)
class Brick:
    sort_index: int = field(init=False, repr=False)
    x: int
    y: int
    z: int
    
    def __post_init__(self):
        self.sort_index = min(self.z)
        self.supports = set()
        self.supported_by = set()
        
    def __repr__(self) -> str:
        return f"Brick({self.id} , supports: {len(self.supports)} blocks, supported by: {len(self.supported_by)} blocks)\n"

def parse_input(input: [str]) -> [Brick]:
    bricks = []
    for line in input:
        start, end = line.split("~")
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))
        x, y, z = [(a, b) for a,  b, in zip(start, end)]
        bricks.append(Brick(x, y, z))
    return bricks

# Bricks overlap when their x and y coordinates overlap
def overlaps(a: Brick, b: Brick) -> bool:
    return max(a.x[0], b.x[0]) <= min(a.x[1], b.x[1]) and max(a.y[0], b.y[0]) <= min(a.y[1], b.y[1])

# Something I learned on day 19, lists hold references to objects. So we can directly modify the objects in the list. No need to return a new list
def brick_fall(bricks: [Brick]):
    for i, brick in enumerate(bricks):
        dz = 1
        for b in bricks[:i]:
            if overlaps(brick, b):
                dz = max(dz, b.z[1] + 1)
        temp = brick.z[1]
        temp -= brick.z[0] - dz
        new_z = (dz, temp)
        brick.z = new_z

# Finds the Bricks that support each other
def find_supports(bricks: [Brick]):
    for i, brick in enumerate(bricks):
        for b in bricks[:i]:
            if overlaps(brick, b) and brick.z[0] == b.z[1] + 1:
                b.supports.add(brick)
                brick.supported_by.add(b)

def part1(bricks: [Brick]) -> int:
    sorted_bricks = sorted(bricks)
    brick_fall(sorted_bricks)
    f = sorted(sorted_bricks)
    find_supports(f)
    
    total = 0
    for brick in f:
        # We go through all the bricks we support and check if they are supported by at least 2 bricks
        # If they are, we can disintegrate it
        if all(len(b.supported_by) >= 2 for b in brick.supports):
            total += 1
    return total

def part2(bricks: [Brick]) -> int :
    sorted_bricks = sorted(bricks)
    brick_fall(sorted_bricks)
    f = sorted(sorted_bricks)
    find_supports(f)
    
    total = 0
    for brick in f:
        queue = deque(b for b in brick.supports if len(b.supported_by) == 1)
        seen = set(queue)
        seen.add(brick)
        
        while queue:
            b = queue.popleft()
            
            for s in b.supports.difference(seen):
                if s.supported_by.issubset(seen):
                    queue.append(s)
                    seen.add(s)
                    
        total += len(seen) - 1 # We don't want to count the brick we started with
    return total

# Takes about 1.4 seconds for each part to run, I'm sure there's a way to optimize it, but by brain is barely working on day 22 🤕
# Now it's they're running in 1 second each. Guess using set functions is faster than  using operators (?) 🤷
# Also learned how to add emojis to my code 😎
def main():
    input = open("input.txt", "r").read().splitlines()
    b = parse_input(input)
    t1 = process_time()
    part1_sum = part1(b)
    t2 = process_time()
    print(f"Part 1: {part1_sum}")
    print(f"Part 1 took: {t2 - t1} seconds")
    
    b = parse_input(input)
    t1 = process_time()
    part2_sum = part2(b)
    t2 = process_time()
    print(f"Part 2: {part2_sum}")
    print(f"Part 2 took: {t2 - t1} seconds")

if __name__ == "__main__":
    main()