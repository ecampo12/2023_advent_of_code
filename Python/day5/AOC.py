import re
import time

def parse_input(input):
    sections = re.split(r'\n\s*\n', input)
    seeds = [int(seed) for seed in re.findall(r"\d+", sections.pop(0))]
    return seeds, sections

def part1(input):
    locations, paths  = [], []
    seeds, maps = parse_input(input)

    for seed in seeds:
        path = []
        for map in maps:
            map = map.splitlines()[1:]
            path.append(seed)
            for desc in map:
                dest_start, source_start, range_len = [int(value) for value in re.findall(r"\d+", desc)]
                if seed in range(source_start, source_start + range_len): # learned this trick today
                    seed = dest_start + (seed - source_start)
                    break
        else: # learned this trick today, else after for loop
            path.append(seed)        
            paths.append(path)
            locations.append(seed)
    return locations, paths

def part2(input):
    seeds, maps = parse_input(input)
    new_seeds = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
    
    for map in maps:
        map = map.splitlines()[1:]
        ranges = []
        for desc in map:
            values = [int(value) for value in re.findall(r"\d+", desc)]
            ranges.append(values)
        
        locations = []
        while len(new_seeds) > 0:
            start, end = new_seeds.pop()
            # checking overlapping ranges
            for dest_start, source_start, range_len in ranges:
                overlap_start = max(start, source_start)
                overlap_end = min(end, source_start + range_len)
                if overlap_start < overlap_end:
                    new_start = dest_start + (overlap_start - source_start)
                    new_end = dest_start + (overlap_end - source_start)
                    locations.append((new_start, new_end))
                    if overlap_start > start:
                        new_seeds.append((start, overlap_start))
                    if end > overlap_end:
                        new_seeds.append((overlap_end, end))
                    break
            else: # apprently this is a thing in python (else after for loop)
                locations.append((start, end))
        new_seeds = locations
    return new_seeds

def main():
    input = open("input.txt", "r").read()
    start_p1 = time.perf_counter()
    locations, _ = part1(input)
    part1_answer = min(locations)
    end_p1 = time.perf_counter()
    
    start_p2 = time.perf_counter()
    locations = part2(input)
    part2_answer = min(locations)[0]
    end_p2 = time.perf_counter()
    
    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")
    print("="*15)
    print(f"Took {end_p1 - start_p1:0.4f} seconds to solve part 1")
    print(f"Took {end_p2 - start_p2:0.4f} seconds to solve part 2")

if __name__ == "__main__":
    main()