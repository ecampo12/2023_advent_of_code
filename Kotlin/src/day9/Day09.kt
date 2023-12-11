package day9
import readInput

fun main() {
    fun parseInput(input: List<String>): List<List<Int>> {
        return input.map{
            val map = it.split(" ").map { s ->
                val int = s.toInt()
                int
            }
            map
        }
    }

    fun getNextNumber(input: List<Int>): Int {
        if (input.all { it == 0 })
            return 0
        return getNextNumber(input.mapIndexed { index, i ->
            if (index == 0) {
                0
            } else {
                i - input[index - 1]
            }
        }.drop(1)) + input.last()
    }
    fun part1(input: List<List<Int>>): Int {
        val nextNumbs = ArrayList<Int>()
        for (line in input) {
            nextNumbs.add(getNextNumber(line))
        }
        return nextNumbs.sum()
    }

    fun part2(input: List<List<Int>>): Int {
        val nextNumbs = ArrayList<Int>()
        for (line in input) {
            nextNumbs.add(getNextNumber(line.reversed()))
        }
        return nextNumbs.sum()
    }

    println("TESTS-----------")
    val testInput = readInput("day9/test_input.txt")
    var x = parseInput(testInput)
    val test1 = part1(x)
    println("Test part 1: $test1")
    check(test1 == 114)

    val test2 = part2(x)
    println("Test part 2: $test2")
    check(test2 == 2)

    println("RUNNING---------")
    val input = readInput("day9/input.txt")
    x = parseInput(input)
    val part1Sum = part1(x)
    println("Part 1: $part1Sum")
    val part2Sum = part2(x)
    println("Part 2: $part2Sum")

}
