import re
def parse_input(input: [str]) -> [(str, int, str)]:
    instructions = []
    for line in input:
        dir, num, hex = line.split(" ")
        instructions.append((dir, int(num), hex))
    return instructions

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

# Learned about shoelace formula : https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem
# Video: https://www.youtube.com/watch?v=0KjG8Pg6LGk
# TL;DR: Area of a polygon is the sum of the absolute value of the products of the coordinates of the vertices, divided by 2
def shoe_lace(points: [(int, int)]) -> int:
    x = [points[i][0] * (points[i - 1][1] - points[i + 1][1]) for i in range(len(points) - 1)]
    return abs(sum(x)) // 2

def part1(input: [(str, int, str)]) -> int:
    curr_loc = (0, 0)
    seen = [curr_loc]
    perimeter = 0
    for dir, num, _ in input:
        perimeter += num
        curr_loc = (curr_loc[0] + directions[dir][0] * num, curr_loc[1] + directions[dir][1] * num)
        seen.append(curr_loc)
        
    area = shoe_lace(seen)
    
    # Using pick's theorem, we can find the number of points inside a polygon
    # https://artofproblemsolving.com/wiki/index.php/Pick%27s_Theorem
    # TL;DR: Area = I + B/2 - 1
    # I = number of points inside the polygon
    # B = number of points on the perimeter of the polygon
    # Rearrange the formula: I = Area - B/2 + 1
    i = area - perimeter // 2 + 1

    # points of the lagoon is just the points inside the polygon + the points on the perimeter
    return i + perimeter

def part2(input: [(str, int, str)]) -> int:
    new_input = []
    dirs = ['R', 'D', 'L', 'U']
    for _,_ , hex in input:
        hex = re.search(r"\w+", hex).group(0)
        new_inst = dirs[int(hex[-1])]
        new_num = int(hex[:-1], 16)
        new_input.append((new_inst, new_num, ""))
    return part1(new_input)

def main():
    input = open("input.txt", "r").read().splitlines()
    x = parse_input(input)
    part1_sum = part1(x)
    part2_sum = part2(x)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()