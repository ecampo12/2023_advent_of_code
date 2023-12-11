import readInput

fun main() {
    fun part1(input: List<String>): Int {
        return 0
    }

    fun part2(input: List<String>): Int {
        return 0
    }

    println("TESTS-----------")
    var testInput = readInput("day1/test_input.txt")
    val test1 = part1(testInput)
    println("Test part 1: $test1")
    check(test1 == 1)

    testInput = readInput("day1/test_input2.txt")
    val test2 = part2(testInput)
    println("Test part 2: $test2")
    check(test2 == 1)

    println("RUNNING---------")
    val input = readInput("day1/input.txt")
    val part1Sum = part1(input)
    println("Part 1: $part1Sum")

    val part2Sum = part2(input)
    println("Part 2: $part2Sum")
    println("Hello world!")
}
