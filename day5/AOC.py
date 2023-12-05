import re
import pprint

class Almanac:
    def __init__(self, seeds):
        self.seeds = [int(seed) for seed in seeds]
    
    def add_map(self, map):
        map = re.match(r"(\w+-\w+-\w+)", map.splitlines()[0])
        print(map.group(1))

def creat_map(input):
    map = {}
    input = input.splitlines()
    name = input.pop(0)
    
    # print(input)
    for desc in input:
        values = [int(value) for value in re.findall(r"\d+", desc)]
        
        dest_start = values[0]
        source_start = values[1]
        range_len = values[2]
        for i in range(range_len):
            map[source_start + i] = dest_start + i
            
    return name, map

def parse_input(input):
    sections = re.split(r'\n\s*\n', input)
    seeds = [int(seed) for seed in re.findall(r"\d+", sections.pop(0))]
    maps = {}
    for sec in sections:
        name, map = creat_map(sec)
        maps[name] = map
    return seeds, maps

def part1(input):
    print("made it here")
    locations = []
    paths = []
    seeds, maps = parse_input(input)
    print("made it past parse_input")
    
    for seed in seeds:
        # print(f"seed: {seed}")
        path = [seed]
        for key, map in maps.items():
            # print(f"key: {key} seed: {seed}")
            if seed not in map:
                pass
            else:
                seed = map[seed]
            path.append(seed)
        paths.append(path)
        locations.append(seed)
    return locations, paths

def part2(input):
    return True

def main():
    input = open("input.txt", "r").read()
    locations, _ = part1(input)
    # print(locations)
    part1_answer = min(locations)
    part2_sum = 0
    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()