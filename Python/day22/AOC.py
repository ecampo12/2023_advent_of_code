from dataclasses import dataclass, field

@dataclass(order=True)
class Brick:
    sort_index: int = field(init=False, repr=False)
    x: int
    y: int
    z: int
    
    def __post_init__(self):
        self.sort_index = min(self.z)
        self.supports = []
        self.supported_by = []
        
    def __repr__(self) -> str:
        return f"Brick({self.x}, {self.y}, {self.z}, supports: {len(self.supports)} blocks, supported by: {len(self.supported_by)} blocks)\n"

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

def find_supports(bricks: [Brick]):
    for i, brick in enumerate(bricks):
        for b in bricks[:i]:
            if overlaps(brick, b) and brick.z[0] == b.z[1] + 1:
                b.supports.append(brick)
                brick.supported_by.append(b)

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

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read().splitlines()
    b = parse_input(input)
    part1_sum = part1(b)
    print(f"Part 1: {part1_sum}")
    part2_sum = 0
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()