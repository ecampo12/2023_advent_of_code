import re
import pprint

def parse_input(input):
    sections = re.split(r'\n\s*\n', input)
    seeds = [int(seed) for seed in re.findall(r"\d+", sections.pop(0))]
    return seeds, sections

def part1(input):
    locations = []
    paths = []
    seeds, maps = parse_input(input)

    for seed in seeds:
        path = []
        for map in maps:
            map = map.splitlines()
            map.pop(0) # remove name of map, not needed
            path.append(seed)
            for desc in map:
                values = [int(value) for value in re.findall(r"\d+", desc)]
                dest_start = values[0]
                source_start = values[1]
                range_len = values[2]
                if seed >= source_start and seed < source_start + range_len:
                    seed = dest_start + (seed - source_start)
                    break
        path.append(seed)        
        paths.append(path)
        locations.append(seed)
    return locations, paths

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read()
    locations, _ = part1(input)
    part1_answer = min(locations)
    part2_sum = 0
    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()