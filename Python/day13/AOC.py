import re

def parse_input(input):
    lines = []
    for x in re.split("\n\n", input):
        lines.append([line for line in x.split("\n") if line != ""])
    return lines

def reverse_list(input):
    rev = []
    for i in range(len(input), 0, -1):
        rev.append(input[i - 1])
    return rev

def get_horizontal(input, sudge=False):
    for row in range(1, len(input)):
        top = reverse_list(input[:row])
        bottom = input[row:]
        
        # makes sure both halfs are the same length
        top = top[:len(bottom)]
        bottom = bottom[:len(top)]
        
        if sudge:
            count = 0
            for i, j in zip(top, bottom):
                for a, b in zip(i, j):
                    if a != b:
                        count += 1
            if count == 1:
                return (row, row + 1)
        elif top == bottom:
            return (row, row + 1) # tuple for debugging
    return (0, 0)
    
def part1(input, smudge=False):
    total = 0
    for pattern in input:
        hor = get_horizontal(pattern, smudge)
        total += hor[0] * 100
        col = get_horizontal(list(zip(*pattern)), smudge) # zip trick to transpose matrix
        total += col[0]
    return total

def part2(input):
    return part1(input, True)

def main():
    input = open("input.txt", "r").read()
    x = parse_input(input)
    part1_sum = part1(x)
    part2_sum = part2(x)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()