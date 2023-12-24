from itertools import combinations
from time import perf_counter
# First day where I had to use a library that wasn't in the standard library
from z3 import Int, Solver, sat # pip install z3-solver

def parse_input(input):
    hail = []
    for line in input:
        points, d = line.split(" @ ")
        points = list(map(int, points.split(", ")))
        d = list(map(int, d.split(", ")))
        hail.append((points, d))
    return hail

def find_line_functions(hail):
    points, d = hail
    x, y, _ = points
    dx, dy, _ = d
    m = dy / dx
    b = y - m * x
    return m, b

def find_intersection(hail1, hail2):
    a, c = find_line_functions(hail1)
    b, d = find_line_functions(hail2)
    
    if a == b: # lines are parallel
        return None, None
    x_intersect = (d - c) / (a - b)
    y_intersect = a * x_intersect + c
    
    return x_intersect, y_intersect
    
def part1(input, bound1, bound2):
    count = 0
    for h1, h2 in combinations(input, 2):
        x, y = find_intersection(h1, h2)
        if x == None:
            continue
        if bound1 <= x <= bound2 and bound1 <= y <= bound2:
            for h in [h1, h2]:
                dx = x - h[0][0]
                dy = y - h[0][1]
                if (dx > 0) != (h[1][0] > 0) or (dy > 0) != (h[1][1] > 0):
                    # The hail is moving away from the intersection, so it happened in the past
                    break
            else:
                count += 1
    return count

# z3 is a SMt solver, I used it to solve a system of equations
# For part 2 I need to find where the rock has to be to destory all the hail over time
# After finding that position, I just need to find the sum of the coordinates of the rock
def part2(input):
    fx,  fy,  fz  = Int("fx"),  Int("fy"),  Int("fz")
    fdx, fdy, fdz = Int("fdx"), Int("fdy"), Int("fdz")
    s = Solver()
    # Appreantly we don't need to check all the hail.
    # The first few is enough, plus it solves 0.25 seconds faster 🤷 
    for i, ((x,y,z), (dx,dy,dz)) in enumerate(input[:10]):
        t = Int(f"t{i}")
        s.add(t >= 0)
        s.add(x + dx * t == fx + fdx * t)
        s.add(y + dy * t == fy + fdy * t)
        s.add(z + dz * t == fz + fdz * t)
    if s.check() == sat:
        return s.model().eval(fx + fy + fz)
    return 0

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(parse_input(input), 200000000000000, 400000000000000)
    print(f"Part 1: {part1_sum}")
    
    t1 = perf_counter()
    part2_sum = part2(parse_input(input))
    t2 = perf_counter()
    print(f"Part 2: {part2_sum}")
    print(f"Part 2 took {t2 - t1} seconds")

if __name__ == "__main__":
    main()