import kotlin.math.absoluteValue

data class Instruction(val dir: String, val num: Int, val hex: String)
fun main() {
    fun parseInput(input: List<String>): List<Instruction> {
        return input.map{
            val dir = it.split(" ")[0]
            val num = it.split(" ")[1].toInt()
            val hex = it.split(" ")[2]

             Instruction(dir, num, hex)
        }
    }
    val dirs = mapOf(
        "R" to Pair(0,1),
        "D" to Pair(1, 0),
        "L" to  Pair(0, -1),
        "U" to Pair(-1, 0)
    )

    fun part1(input: List<Instruction>): Long {
        var parameter = 0
        var currLoc = Pair(0L, 0L)
        val cords = ArrayList<Pair<Long, Long>>()
        cords.add(currLoc)
        input.forEach {
            parameter += it.num
            currLoc = Pair(
                currLoc.first + dirs[it.dir]!!.first * it.num,
                currLoc.second + dirs[it.dir]!!.second * it.num
            )
            cords.add(currLoc)
        }

        // This monstrosity is just the combined Shoelace theorem and pick's theorem combined.
        // We add the parameter back in the end to get all points of the lagoon
        return (((1 until cords.size - 1).sumOf { i ->
            cords[i].first * (cords[i - 1].second - cords[i + 1].second)
        } / 2).absoluteValue - (parameter / 2) + 1 + parameter).toLong()
    }

    fun part2(input: List<Instruction>): Long  {
        val dirMap = dirs.map { it.key }
        println(dirMap)
        val instructions = input.map {
            val x = "\\w+".toRegex().find(it.hex)!!.value
            val newDir = dirMap[x.last().digitToInt()]
            val newNum = Integer.valueOf(x.subSequence(0, x.count()-1).toString(), 16)
            Instruction(newDir, newNum, "")
        }
        return part1(instructions)
    }

    println("TESTS-----------")
    val testInput = readInput("day18/test_input.txt")
    val x = parseInput(testInput)
    val test1 = part1(x)
    println("Test part 1: $test1")
    check(test1 == 62L)

    val test2 = part2(x)
    println("Test part 2: $test2")
    check(test2 == 952408144115)

    println("RUNNING---------")
    val input = readInput("day18/input.txt")
    val y = parseInput(input)
    val part1Sum = part1(y)
    println("Part 1: $part1Sum")

    val part2Sum = part2(y)
    println("Part 2: $part2Sum")
}
