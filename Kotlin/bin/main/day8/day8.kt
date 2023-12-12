import kotlin.math.abs

data class DesertMap(val instructions: List<String>, val network: Map<String, Pair<String, String>>)
fun main() {
    fun parseInput(input: List<String>): DesertMap {
        val network = HashMap<String, Pair<String, String>>()
        val instructions = input[0].map { it.toString() }.toList()
        for (i in 2..<input.count()){
            val x = "\\w+".toRegex().findAll(input[i]).map{it.value }.toList()
            network[x[0]] = Pair(x[1], x[2])
        }
        return DesertMap(instructions, network)
    }

    fun part1(input: DesertMap): Int {
        var currInst = input.instructions[0]
        var currLoc = "AAA"
        var count = 1
        while (currLoc != "ZZZ"){
            currLoc = if (currInst == "L") {
                input.network[currLoc]!!.first
            } else {
                input.network[currLoc]!!.second
            }
            currInst = input.instructions[count % input.instructions.count()]
            count++
        }
        return count - 1
    }

    fun gcd(a: Long, b: Long): Long {
        return if (b == 0L) a else gcd(b, a % b)
    }

    fun lcm(a: Long, b: Long): Long {
        return if (a == 0L || b == 0L) 0L else abs(a * b) / gcd(a, b)
    }

    fun findLCM(numbers: List<Long>): Long {
        return numbers.reduce { acc, num -> lcm(acc, num) }
    }

    fun part2(input: DesertMap): Long {
        var currInst = input.instructions[0]
        val counts = ArrayList<Int>()
        val startNodes = input.network.keys.filter { it.last() == 'A' }
        for (node in startNodes){
            var currNode = node
            var count = 1
            while (true) {
                currNode = if (currInst == "L") {
                    input.network[currNode]!!.first
                } else {
                    input.network[currNode]!!.second
                }
                currInst = input.instructions[count % input.instructions.count()]
                count++
                if (currNode.last() == 'Z') break
            }
            counts.add(count - 1)
        }
        return findLCM(counts.map { it.toLong() })
    }

    println("TESTS-----------")
    var testInput = readInput("day8/test_input.txt")
    var x = parseInput(testInput)
    val test1 = part1(x)
    println("Test part 1: $test1")
    check(test1 == 6)

    testInput = readInput("day8/test_input2.txt")
    x = parseInput(testInput)
    val test2 = part2(x)
    println("Test part 2: $test2")
    check(test2 == 6L)

    println("RUNNING---------")
    val input = readInput("day8/input.txt")
    val y = parseInput(input)
    val part1Sum = part1(y)
    println("Part 1: $part1Sum")

    val part2Sum = part2(y)
    println("Part 2: $part2Sum")
}
