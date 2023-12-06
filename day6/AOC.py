import re

def parse_input(input):
    records = input.splitlines()
    times = re.findall(r"(\d+)", records[0].split(":")[1])
    distances = re.findall(r"(\d+)", records[1].split(":")[1])
    return times, distances

# Kinda brute force, but it works
def part1(times, distances):
    times = [int(time) for time in times]
    distances = [int(distance) for distance in distances]
    prod = 1
    for time, distance in zip(times, distances):
        possible_wins = [] # for debugging
        for i in range(1, time):
            if (time-i)*i > distance:
                possible_wins.append((i, (time-i)*i))
                
        prod *= len(possible_wins)
            
    return prod

# Again, kinda brute force, but it works
def part2(times, distances):
    times = int("".join(str(time) for time in times))
    distances = int("".join(str(distance) for distance in distances))
    count = 0
    for i in range(1, times):
        if (times-i)*i > distances:
            count += 1
    return count

def main():
    input = open("input.txt", "r").read()
    time, distance = parse_input(input)
    part1_prod = part1(time, distance)
    part2_sum = part2(time, distance)
    print(f"Part 1: {part1_prod}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()