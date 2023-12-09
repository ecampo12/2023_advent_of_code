import Foundation

struct Schematic {
    let partNumbers: [Part]
    let symbols: [Symbol]
    let gears: [Symbol]

    init(input: [String]) {
        let symbolList = ["*", "$", "+", "/", "@", "#", "%", "&", "-", "="]
        var symbols: [Symbol] = []
        var partNumbers: [Part] = []
        var gears: [Symbol] = []
        for row in 0..<input.count {
            var numIndexStart = 0
            var numIndexEnd = 0
            var number = ""
            for index in 0..<input[row].count {
                let charIndex  = input[row].index(input[row].startIndex, offsetBy: index )
                let char = String(input[row][charIndex])
                if let _ = Int(char) {
                    if number.isEmpty {
                        numIndexStart = index
                    }
                    number.append(char)
                }
                if let _ = symbolList.firstIndex(of: char) {
                    let symbol = Symbol(symbol: char, row: row, index: index)
                    if char == "*" {
                        gears.append(symbol)
                    }
                    symbols.append(Symbol(symbol: String(char), row: row, index: index))
                    if !number.isEmpty {
                        numIndexEnd = index
                        partNumbers.append(Part(partNumber: Int(number)!, row: row, indeices: numIndexStart..<numIndexEnd))
                        number = ""
                    }
                    numIndexStart = 0
                }
                if char == "." {
                    numIndexEnd = index
                    if !number.isEmpty {
                        partNumbers.append(Part(partNumber: Int(number)!, row: row, indeices: numIndexStart..<numIndexEnd))
                        number = ""
                    }
                }
            }
            if !number.isEmpty {
                numIndexEnd = input[row].count
                partNumbers.append(Part(partNumber: Int(number)!, row: row, indeices: numIndexStart..<numIndexEnd))
                number = ""
            }
    }
    self.partNumbers = partNumbers
    self.symbols = symbols
    self.gears = gears
}

    func getAdjacentParts(symbol: Symbol) -> [Part] {
        let positions = [
            (symbol.row - 1, symbol.index - 1),
            (symbol.row - 1, symbol.index),
            (symbol.row - 1, symbol.index + 1),
            (symbol.row, symbol.index - 1),
            (symbol.row, symbol.index + 1),
            (symbol.row + 1, symbol.index - 1),
            (symbol.row + 1, symbol.index),
            (symbol.row + 1, symbol.index + 1),
        ]
        return partNumbers.filter { part in
            positions.contains { position in
                part.row == position.0 && part.indeices.contains(position.1)
            }
        }
    }
}

struct Part {
    let partNumber: Int
    let row: Int
    let indeices: Range<Int>
}

extension Part: Hashable {
    func hash(into hasher: inout Hasher) {
        hasher.combine(partNumber)
    }
}

struct Symbol {
    let symbol: String
    let row: Int
    let index: Int
}

func part1(input: [String]) -> Int {
    let schematic = Schematic(input: input)
    return schematic.symbols.map { schematic.getAdjacentParts(symbol: $0) }.reduce(0) { $0 + $1.reduce(0) { $0 + $1.partNumber } }
}

func part2(input: [String]) -> Int {
    let schematic = Schematic(input: input)
    // calls to getAdjacentParts twice for each gear because I do not keep of the neighbors of the gears
    return schematic.gears.filter { schematic.getAdjacentParts(symbol: $0).count == 2 }.map { schematic.getAdjacentParts(symbol: $0) }.reduce(0) { $0 + $1.reduce(1) { $0 * $1.partNumber } }
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