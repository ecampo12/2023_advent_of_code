func part1(input: [String]) -> Int {
    var nums: [Int] = []
    input.forEach{
        let vals = $0.map{Int(String($0))}.filter{$0 != nil}.map{$0!}
        nums.append((vals.first! )*10 + vals.last!)
    }
    return nums.reduce(0, +)
}

func part2(input: [String]) -> Int {
    let wordToInt = ["one": "o1e", "two": "t2o", "three": "th3ee", "four": "f4ur", "five": "f5ve",
                     "six": "s6x", "seven": "se7en", "eight": "ei8gh", "nine": "n9ne"]
    var nums: [Int] = []
    input.forEach{
        var str = $0

        for (key, value) in wordToInt {
            if str.contains(key){
                str.ranges(of: key).forEach{
                    str.replaceSubrange($0, with: value)               
                }
            }
        }
        let vals = str.map{Int(String($0))}.filter{$0 != nil}.map{$0!}
        nums.append((vals.first! )*10 + vals.last!)
    }
    return nums.reduce(0, +)
}

print("Testing------------------")
let part1_example = part1(input: InputData.example)
print("Part1 Testing: \(part1_example)")
let part2_example = part2(input: InputData.example2)
print("Part2 Testing: \(part2_example)")

print("Running------------------")
let part1_sum = part1(input: InputData.challenge)
print("Part1: \(part1_sum)")
let part2_sum = part2(input: InputData.challenge)
print("Part2: \(part2_sum)")