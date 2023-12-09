import Foundation

struct Card {
    var id: Int
    var winningNums: [Int]
    var ourNums: [Int]
}

func parseInput(input: [String]) -> [Card] {
    return input.map({line in
        let id = Int(line.split(separator: ":")[0].split(separator: " ")[1])!
        let winnings = line.split(separator: "|")[0].split(separator: " ")[2...].map{Int($0)!}
        let numbers = line.split(separator: "|")[1].split(separator: " ").map{Int($0)!}
        return Card(id: id, winningNums: winnings , ourNums: numbers)
    })
}

func part1(input: [String]) -> Int {
    return parseInput(input: input).reduce(0, {sum, card in
        let exponent = Double(card.winningNums.filter({card.ourNums.contains($0)}).count - 1)
        return sum + (exponent >= 0 ? Int(pow(2.0, exponent)) : 0)
    })
}

func part2(input: [String]) -> Int {
    let cards = parseInput(input: input)
    var cardMap = cards.reduce(into: [Int: Int](), {map, card in map[card.id] = 1})
    cards.forEach{card in
        let winningNums = card.winningNums.filter({card.ourNums.contains($0)}).count
        if winningNums != 0 {
            (1...winningNums).forEach{num in
                cardMap[card.id+num]! += 1 * cardMap[card.id]!
            }
        }
    } 
    return cardMap.reduce(0, {$0 + $1.value})
}

print("Testing------------------")
let part1_example = part1(input: InputData.example)
print("Part1 Testing: \(part1_example)")
let part2_example = part2(input: InputData.example)
print("Part2 Testing: \(part2_example)")

print("Running------------------")
let part1_sum = part1(input: InputData.challenge)
print("Part1: \(part1_sum)")
let part2_sum = part2(input: InputData.challenge)
print("Part2: \(part2_sum)")