import re
from itertools import combinations

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
    x2, y2 = x + dx, y + dy
    m = (y2 - y) / (x2 - x)
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
        if x >= bound1 and x <= bound2 and y >= bound1 and y <= bound2:
            for h in [h1, h2]:
                dx = x - h[0][0]
                dy = y - h[0][1]
                if (dx > 0) != (h[1][0] > 0) or (dy > 0) != (h[1][1] > 0):
                    break
            else:
                count += 1
    return count

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(parse_input(input), 200000000000000, 400000000000000)
    part2_sum = 0
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()