import re

RED = 12
GREEN = 13
BLUE = 14

def get_colors(input):
    game_sets = input.split(":")[1].split(";")
    return [re.findall(r"(\d+ (blue|red|green))", game_set) for game_set in game_sets]
        

def part1(input):
    colors = get_colors(input)
    for color in colors:
        for c in color:
            num = int(c[0].split(" ")[0])
            if c[1] == "red" and num > RED:
                return False
            elif c[1] == "blue" and num > BLUE:
               return False
            elif c[1] == "green" and num > GREEN:
                return False
    return True

def part2(input):
    colors = get_colors(input)
    fewest_red, fewest_green, fewest_blue = 0, 0, 0
    for color in colors:
        for c in color:
            num = int(c[0].split(" ")[0])
            if c[1] == "red" and num > fewest_red:
                fewest_red = num
            elif c[1] == "blue" and num > fewest_blue:
                fewest_blue = num
            elif c[1] == "green" and num > fewest_green:
                fewest_green = num
    return fewest_red * fewest_green * fewest_blue

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum, part2_sum = 0, 0
    for i in range(len(input)):
        if part1(input[i]):
            part1_sum += i + 1
        part2_sum += part2(input[i])

    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()