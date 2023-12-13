import functools
import time

def parse_input(input):
    springs, con_groups = input.split(" ")
    con_groups = tuple(map(int, con_groups.split(","))) # Needed to make the function cache work
    return springs, con_groups

# This was tricky to figure out, but I think I got it
# General approach:
#   Base case 1: If we have no springs left, and no numbers left, we have a valid arrangement
#   Base case 2: If we have no numbers left, but still have springs, we have an invalid arrangement
#   Recursive case 1: If we have a spring start with a dot or a question mark, we slice the front off the springs, 
#                     and check the rest of the springs with the same numbers
#   Recursive case 2: If we have a spring start with a hash or a question mark, we do some check and slice x number of springs off. 
#                     We pass the rest of the springs and drop the first number off the numbers list. 
# This is a decorator that caches the results of the function, needed to make part 2 run in a reasonable amount of time
@functools.cache 
def find_arrangements(springs, numbers):
    if springs == "":                                   # If we have no springs left, and no numbers left, we have a valid arrangement
        return 1 if numbers == () else 0
    if numbers == ():                                   # If we have no numbers left, but still have springs, we have an invalid arrangement
        return 0 if "#" in springs else 1

    count = 0
        
    if springs[0] in [".", "?"]:                                # If we have a spring start with a dot or a question mark...
        count += find_arrangements(springs[1:], numbers)        # We slice the front off the springs, and check the rest of the springs with the same numbers
    if springs[0] in ["#", "?"]:                                # If we have a spring start with a hash or a question mark...
        # print(f"Spring: {springs}, numbers: {numbers}")
        contains = "." not in springs[:numbers[0]]              # Check to see if the springs have dots
        if numbers[0] <= len(springs) and contains:                     # Check to make sure the numbre of damaged springs is less than the number of springs, else we get an index error
            if (numbers[0] == len(springs) or springs[numbers[0]] != "#"):  # Need to make sure we have things left to check or make sure we aren't checking mid damanged spring
                count += find_arrangements(springs[numbers[0] + 1:], numbers[1:])

    return count


def part1(input):
    total = 0
    for line in input:
        springs, con_groups = parse_input(line)
        total += find_arrangements(springs, con_groups)
        # print("-"*10)
    return total

def part2(input):
    total = 0
    for line in input:
        springs, con_groups = parse_input(line)
        springs = "?".join([springs]*5)
        con_groups *= 5
        total += find_arrangements(springs, con_groups)
    return total

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum = part1(input)
    print(f"Part 1: {part1_sum}")
    
    t1 = time.perf_counter()
    part2_sum = part2(input)
    t2 = time.perf_counter()
    print(f"Part 2: {part2_sum}")

    print(f"Part 2 took {t2 - t1} seconds")
    
if __name__ == "__main__":
    main()