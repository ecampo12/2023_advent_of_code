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

def main():
    input = open("input.txt", "r").read().splitlines()
    sum = 0
    for i in range(len(input)):
        if part1(input[i]):
            sum += i + 1

    print(f"Part 1: {sum}")

if __name__ == "__main__":
    main()