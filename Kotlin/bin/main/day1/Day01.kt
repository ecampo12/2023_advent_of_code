package day1

import readInput

fun main() {
    fun part1(input: List<String>): Int {
        return input.map { s ->
            val y = s.filter {
                it.isDigit()
            }
            y.first() + "" + y.last()
        }.sumOf { it.toInt() }
    }

    fun part2(input: List<String>): Int {
        val words = mapOf<String, String>("one" to "o1e", "two" to "t2o", "three" to "th3ee",
                "four" to "fo4r", "five" to "fi5e", "six" to "s6x", "seven" to "se7en", "eight" to
                "ei8th", "nine" to "n9ne")
        val modInput = ArrayList<String>()
        input.map{
            var s = it
            for ((k, v) in words) {
                s = s.replace(k, v)
//                println(s)
            }
            modInput.add(s)
        }
//        println(modInput)
        return part1(modInput)
    }

    println("TESTS-----------")
    var testInput = readInput("day1/test_input.txt")
    val test1 = part1(testInput)
    println("Test part 1: $test1")
    check(test1 == 142)

    testInput = readInput("day1/test_input2.txt")
    val test2 = part2(testInput)
    println("Test part 2: $test2")
    check(test2 == 281)

    println("RUNNING---------")
    val input = readInput("day1/input.txt")
    val part1Sum = part1(input)
    println("Part 1: $part1Sum")

    val part2Sum = part2(input)
    println("Part 2: $part2Sum")
    println("Hello world!")
}
