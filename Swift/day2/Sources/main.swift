import Foundation
import RegexBuilder

func part1(input: [String]) -> Int {
    return input.map{
        let game = Int($0.split(separator: ":")[0].split(separator: " ")[1])!
        let valid = $0.split(separator: ":")[1].split(separator: ";").map{String($0)}.map{$0.split(separator: ",")}.map{
            let x = $0.map{
                let cube = $0.split(separator: " ")
                if cube[1] == ("red") && Int(cube[0])! > 12 {
                    return false
                }
                if cube[1] == ("green") && Int(cube[0])! > 13 {
                    return false
                }
                if cube[1] == ("blue") && Int(cube[0])! > 14 {
                    return false
                }
                return true
            }
            return x
         }.map{
             $0.allSatisfy{($0 == true)}
        }.allSatisfy({$0 == true})
        if valid {
            // print("\(game) is valid")
            return game
        }
        return 0
    }.reduce(0, +)
}

func part2(input: [String]) -> Int {
    let blue = #/
    (?<num> \d+)
    (?<color> \sblue)
    /#
    let red = #/
    (?<num> \d+)
    (?<color> \sred)
    /#

    let green = #/
    (?<num> \d+)
    (?<color> \sgreen)
    /#
    return input.map{
        let blues = $0.matches(of: blue).map{ Int($0.num)! }
        let reds = $0.matches(of: red).map{ Int($0.num)! }
        let greens = $0.matches(of: green).map{ Int($0.num)! }
        
        return blues.max()! * reds.max()! * greens.max()!
    }.reduce(0, +)    
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