import re

RED = 12
GREEN = 13
BLUE = 14

def part1(input):
    game_sets = input.split(":")[1].split(";")

    for game_set in game_sets:
        colors = re.findall(r"(\d+ (blue|red|green))", game_set)
        for color in colors:
            num = int(color[0].split(" ")[0])
            if color[1] == "red" and int(num) > RED:
                return False
            elif color[1] == "blue" and int(num) > BLUE:
               return False
            elif color[1] == "green" and int(num) > GREEN:
                return False

    return True

def part2(input):
    game_sets = input.split(":")[1].split(";")

    fewest_red, fewest_green, fewest_blue = 0, 0, 0
    for game_set in game_sets:
        colors = re.findall(r"(\d+ (blue|red|green))", game_set)
        for color in colors:
            num = int(color[0].split(" ")[0])
            if color[1] == "red" and int(num) > fewest_red:
                fewest_red = num
            elif color[1] == "blue" and int(num) > fewest_blue:
                fewest_blue = num
            elif color[1] == "green" and int(num) > fewest_green:
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