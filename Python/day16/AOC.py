import time

# (y, x)
up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)
    
def part1(input, start_row = 0, start_col = -1, start_dir = right):
    energized = set()
    beams = [(start_row, start_col, start_dir)] # could use a deque here, but it doesn't spped part 2 up much. 
    x_bound, y_bound = len(input[0]), len(input)
    while beams:
        row, col, dir = beams.pop()
        
        row += dir[0]
        col += dir[1]
        
        if 0 <= row < y_bound and 0 <= col < x_bound:
            char = input[row][col]
            if char == "." or (char == "-" and dir[1] != 0) or (char == "|" and dir[0] != 0):
                pass # keep going if empty space or traveling along splitter
            elif char == "/":
                dir = (-dir[1], -dir[0])
            elif char == "\\":
                dir = (dir[1], dir[0])
            else:
                for dir in [up, down] if char == "|" else [left, right]: # if it not "|" then it must be "-"
                    if (row, col, dir) not in energized:                 # just loop and deal with the other directions
                        beams.append((row, col, dir))
                        energized.add((row, col, dir))
                        
            if (row, col, dir) not in energized:
                    beams.append((row, col, dir))
                    energized.add((row, col, dir))
        
    energized = {(row, col) for (row, col, _) in energized}
    return len(energized)

# Meh, we'll just brute force it
def part2(input):
    max_vals = []
    for row in range(len(input)):
        max_vals.append(part1(input, row))
        max_vals.append(part1(input, row, len(input), left))
    
    for col in range(len(input)):
        max_vals.append(part1(input, -1, col, down))
        max_vals.append(part1(input, len(input[0]), col, up))
        
    return max(max_vals)

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input)
    print(f"Part 1: {part1_sum}")
    
    t1 = time.perf_counter()
    part2_sum = part2(input)
    t2 = time.perf_counter()
    print(f"Part 2: {part2_sum}")
    print(f"Took Part 2: {t2 - t1} seconds")

if __name__ == "__main__":
    main()