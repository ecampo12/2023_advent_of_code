import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

data class Image(val galaxies: Map<Int, Pair<Int, Int>>, val emptyRows: Set<Int>, val emptyCols: Set<Int>)

fun main() {
    fun parseInput(input: List<String>): Image{
        val galaxies = HashMap<Int, Pair<Int, Int>>()
        var count = 1
        val emptyRows = mutableSetOf<Int>()
        val emptyCols = mutableSetOf<Int>()

        for (i in 0..<input.count()) {emptyRows.add(i)}
        for (i in 0..<input.count()) {emptyCols.add(i)}

        for (row in input.indices){
            for (col in input[row].indices){
                if(input[row][col] == '#'){
                    galaxies[count] = Pair(row, col)
                    emptyRows.remove(row)
                    emptyCols.remove(col)
                    count++
                }
            }
        }
        return Image(galaxies, emptyRows, emptyCols)
    }

    fun findAllGalaxyPairs(galaxyIds: List<Int>): List<Pair<Int, Int>> {
        return galaxyIds.flatMap { id1 ->
            galaxyIds.filter { it != id1 }.map { id2 ->
                id1 to id2
            }
        }.distinctBy { (id1, id2) ->
            setOf(id1, id2)
        }
    }

    fun distance(start: Pair<Int, Int>, end: Pair<Int, Int>, emptyRows: Set<Int>, emptyCols: Set<Int>, expand:Long = 2): Long{
        val manhattanDist = abs(start.first - end.first) + abs(start.second - end.second)
        var rowCrossing = 0
        var colCrossing = 0
        for (i in min(start.first, end.first)..<max(start.first, end.first)){
            if (i in emptyRows){ rowCrossing++ }
        }

        for (i in min(start.second, end.second)..<max(start.second, end.second)){
            if ( i in emptyCols) { colCrossing++ }
        }
        return manhattanDist + (expand - 1)*rowCrossing + (expand-1)*colCrossing
    }

    fun part1(image: Image): Long {
        return findAllGalaxyPairs(image.galaxies.keys.toList()).sumOf {
            image.galaxies[it.first]?.let { it1 ->
                image.galaxies[it.second]?.let { it2 ->
                    distance(
                        it1,
                        it2, image.emptyRows, image.emptyCols
                    )
                }
            }!!
        }
    }

    fun part2(image: Image, expand: Long = 2): Long {
        return findAllGalaxyPairs(image.galaxies.keys.toList()).sumOf {
            image.galaxies[it.first]?.let { it1 ->
                image.galaxies[it.second]?.let { it2 ->
                    distance(
                        it1,
                        it2, image.emptyRows, image.emptyCols, expand
                    )
                }
            }!!
        }
    }

    println("TESTS-----------")
    val testInput = readInput("day11/test_input.txt")
    val x = parseInput(testInput)
    val test1 = part1(x)
    println("Test part 1: $test1")
    check(test1.toInt() == 374)

    var test2 = part2(x)
    check(test2 == 374L)

    test2 = part2(x, 10)
    check(test2 == 1030L)

    test2 = part2(x, 100)
    check(test2 == 8410L)

    println("All part2 tests pass!")

    println("RUNNING---------")
    val input = readInput("day11/input.txt")
    val y = parseInput(input)
    val part1Sum = part1(y)
    println("Part 1: $part1Sum")

    val part2Sum = part2(y, 1000000)
    println("Part 2: $part2Sum")
}
