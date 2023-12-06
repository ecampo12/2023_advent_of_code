import re
import time
import math

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

# optimized solution, decreased runtime from 3.4s to 0.0001s
def part2(times, distances):
    times = int("".join(str(time) for time in times))
    distances = int("".join(str(distance) for distance in distances))
 
    # figured out the formula for this one, finally got to use my the quadratic formula
    # (b - x) * x > c (from part1 loop)
    # x^2 - b*x + c < 0
    a = times / 2.0
    b = math.sqrt(a*a - distances)   
    return math.ceil(a + b - 1) - math.floor(a - b + 1) + 1

def main():
    input = open("input.txt", "r").read()
    start_p1 = time.perf_counter()
    times, distances = parse_input(input)
    part1_prod = part1(times, distances)
    end_p1 = time.perf_counter()
    
    start_p2 = time.perf_counter()
    part2_sum = part2(times, distances)
    print(f"Part 1: {part1_prod}")
    print(f"Part 2: {part2_sum}")
    end_p2 = time.perf_counter()
    
    print("="*15)
    print(f"Took {end_p1 - start_p1:0.4f} seconds to solve part 1")
    print(f"Took {end_p2 - start_p2:0.4f} seconds to solve part 2")

if __name__ == "__main__":
    main()