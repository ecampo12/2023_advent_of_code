data class Line(val springs: String, val numbs: List<Int>)
fun main() {
    fun parseInput(input: String): Line{
        val x = input.split(" ")
        val springs = x[0]
        val numbers = x[1].split(",").map { it.toInt() }

//        println("$springs\t$numbers")
        return Line(springs, numbers)
    }

//    fun findArrangements(springs: String, numbs: List<Int>): Int {
//        if (springs == "") {
//            return if (numbs.isEmpty()) 1 else 0
//        }
//        if (numbs.isEmpty()){
//            return if ("#" in springs) 0 else 1
//        }
//        var count = 0
//
//        if (springs[0] in ".?"){
////            println("found")
////            println("springs: $springs\tnumber: $numbs")
//            count += findArrangements(springs.drop(1), numbs)
//        }
//        if (springs[0] in "#?"){
//            if (numbs[0] <= springs.count() &&
//                "." !in springs.substring(0, numbs[0]) &&
//                (numbs[0] == springs.count() || springs[numbs[0]] != '#')){
//                println("springs: $springs\tnumber: $numbs")
//
//                val start = numbs[0]
//                val end = springs.count()
////                println("Start index: $start\tEnd Index: $end")
//
//                count += findArrangements(springs.substring(start, end), numbs.drop(1))
//            }
//        }
//        return count
//    }

    fun findArrangements(springs: String, NUMS: List<Int>): Int {
        if (springs.isEmpty()) {
            return if (NUMS.isEmpty()) 1 else 0
        }

        if (NUMS.isEmpty()) {
            return if ('#' in springs) 0 else 1
        }

        var count = 0

        if (springs[0] in ".?") {
            count += findArrangements(springs.substring(1), NUMS)
        }

        if (springs[0] in "#?") {
            if (NUMS[0] <= springs.length && '.' !in springs.substring(0, NUMS[0]) &&
                (NUMS[0] == springs.length || springs[NUMS[0]] != '#')
            ) {
                println("Springs: $springs\tNUM: $NUMS")
                count += findArrangements(springs.substring(NUMS[0]+1), NUMS.drop(1))
            }
        }

        return count
    }

    fun part1(input: List<String>): Int {
        val total = ArrayList<Int>()
        for (line in input){
            val x = parseInput(line)
//            total += findArrangements(x.springs, x.numbs)
            total.add(findArrangements(x.springs, x.numbs))
            println("-".repeat(10))
        }
        println(total)
        return total.sum()
    }

//    fun part2(input: List<String>): Int {
//        return 0
//    }

    println("TESTS-----------")
    val testInput = readInput("day12/test_input.txt")
    val test1 = part1(testInput)
    println("Test part 1: $test1")
    check(test1 == 21)

//    testInput = readInput("day1/test_input2.txt")
//    val test2 = part2(testInput)
//    println("Test part 2: $test2")
//    check(test2 == 1)
//
//    println("RUNNING---------")
//    val input = readInput("day1/input.txt")
//    val part1Sum = part1(input)
//    println("Part 1: $part1Sum")
//
//    val part2Sum = part2(input)
//    println("Part 2: $part2Sum")
}
