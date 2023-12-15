import re

def hash(input):
    curr = 0
    for ch in input:
        curr += ord(ch)
        curr = (curr * 17) % 256
    return curr

def part1(input):
    return sum(map(hash, input))

def part2(input):
    hash_map = {}
    for val in input:
        if "=" in val:
            lable, _ = val.split("=")
            index = hash(lable)
            if index not in hash_map:
                hash_map[index] = [val]
            else:
                for i in range(len(hash_map[index])):
                    if hash_map[index][i].split("=")[0] == lable:
                        hash_map[index][i] = val
                        break
                else:
                    hash_map[index].append(val)
        else:
            lable, _ = val.split("-")
            index = hash(lable)
            if index not in hash_map:
                continue
            else :
                for i in range(len(hash_map[index])):
                    if hash_map[index][i].split("=")[0] == lable:
                        hash_map[index].pop(i)
                        break
                if len(hash_map[index]) == 0:
                    hash_map.pop(index)
    
    total_power = 0
    for key in hash_map:
        for i, val in enumerate(hash_map[key]):
            _, val = val.split("=")
            power = (key + 1) * (i + 1) * int(val)
            total_power += power
            
    return total_power

def main():
    input = open("input.txt", "r").read().splitlines()[0].split(",")
    part1_sum = part1(input)
    part2_sum = part2(input)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()