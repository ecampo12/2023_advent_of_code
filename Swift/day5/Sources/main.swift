import Foundation

struct Almanac {
    let seeds: [Int]
    let mappings: [Mapping]
}

struct Mapping{
    let id: Int
    let source: [Range<Int>]
    let destination: [Range<Int>]
}

func parseInput(input: [String]) -> Almanac {
    let seeds = input[0].split(separator: " ").map{ Int($0) ?? 0 }.dropFirst().map{Int($0)}
    var id = 0
    let mappings = input[1...].map{
        let lines = $0.split(separator: "\n")
        let map = lines[1...].map{
            let x = $0.split(separator: " ").map{ Int($0)!}
            let dst = x[0]
            let src = x[1]
            let range = x[2]
            return (src..<(src+range), dst..<(dst+range))
        }
        id += 1
        var source: [Range<Int>] = []
        var destination: [Range<Int>] = []
        for (src, dst) in map {
            source.append(src)
            destination.append(dst)
        }
        return Mapping(id: id, source: source, destination: destination)
    }
    return Almanac(seeds: seeds, mappings: mappings)
}
func part1(input: [String]) -> Int {
    let almanac = parseInput(input: input)
    return almanac.seeds.map {
        var newSeed = $0
        for mapping in almanac.mappings{
            let source = mapping.source
            let destination = mapping.destination
            for (src, dst) in zip(source, destination){
                if src.contains(newSeed) {
                    newSeed = dst.lowerBound + newSeed-src.lowerBound
                    break
                }
            }
        }
        return newSeed
    }.min() ?? Int(0)
}

print("Testing------------------")
let part1_example = part1(input: InputData.example)
print("Part1 Testing: \(part1_example)")
// let part2_example = part2(input: InputData.example)
// print("Part2 Testing: \(part2_example)")

// print("Running------------------")
// let part1_sum = part1(input: InputData.challenge)
// print("Part1: \(part1_sum)")
// let part2_sum = part2(input: InputData.challenge)
// print("Part2: \(part2_sum)")