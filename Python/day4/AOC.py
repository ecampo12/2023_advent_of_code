import re

def parse_input(input):
    nums = []
    numbers = input.split(": ")
    card_nums = numbers[1].split(" | ")
    nums.append(re.findall(r'\d+', card_nums[0]))
    nums.append(re.findall(r'\d+', card_nums[1]))
    return nums

def part1(input):
    nums = parse_input(input)
    total = 0
    winning_nums = {}
    winning_nums = {num: 1 for num in nums[0]}
    found_nums = [num for num in nums[1] if num in winning_nums]
    if len(found_nums)-1 >= 0:
        total =2**(len(found_nums)-1)
        
    return found_nums, total

def part2(input):
    # probably more efficient to addto dict as we go, but this works
    card_count = {x: 1 for x in range(len(input))}
    for i in range(len(input)):
            num, _ = part1(input[i])
            for j in range(len(num)):
                if j+i+1 in card_count:
                    card_count[j+i+1] += 1 * card_count[i]      
    return card_count
            
            
def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum, part2_sum = 0, 0
    for i in range(len(input)):
            _, total = part1(input[i])
            part1_sum += total
    cards = part2(input)
    part2_sum = sum([cards[key] for key in cards])
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()