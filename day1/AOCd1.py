import re

NUM_TO_INT = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine' : '9'
    }

def part1(input):
    numbers = re.findall(r'\d', input)
    return int(numbers[0]+numbers[-1])

def part2(input):
    res  = []
    regex = r"(?=(" + "|".join(NUM_TO_INT.keys()) + "|\d))"
    matches = re.findall(regex, input)
    res = [NUM_TO_INT.get(match.lower(), match) for match in matches]
    return int(res[0]+res[-1])

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_sum, part2_sum = 0, 0
    
    for i in range(len(input)):
        part1_sum += part1(input[i])
        part2_sum += part2(input[i])

    print(f'Part 1: {part1_sum}')
    print(f'Part 2: {part2_sum}')

if __name__ == "__main__":
    main()