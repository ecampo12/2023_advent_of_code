import re

def parse_input(input):
    records = input.splitlines()
    times = [int(time) for time in re.findall(r"(\d+)", records[0].split(":")[1])]
    distances = [int(distance) for distance in re.findall(r"(\d+)", records[1].split(":")[1])]
    return times, distances

# Kinda brute force, but it works
def part1(times, distances):
    prod = 1
    for time, distance in zip(times, distances):
        possible_wins = [] # for debugging
        for i in range(1, time):
            if (time-i)*i > distance:
                possible_wins.append((i, (time-i)*i))
                
        print(f"possible wins: {possible_wins}")
        prod *= len(possible_wins)
            
    return prod

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read()
    time, distance = parse_input(input)
    part1_prod = part1(time, distance)
    part2_sum = 0
    print(f"Part 1: {part1_prod}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()