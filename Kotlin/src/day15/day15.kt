data class Lens(val label: String, var focalLen: Int)
class Boxes {
    var boxes = HashMap<Int, ArrayList<Lens>>()

    private fun hash(key: String): Int {
        var currVal = 0
        for (ch in key){
            currVal += ch.code
            currVal = (currVal * 17) % 256
        }
        return currVal
    }

    private fun contains(label: String, index: Int): Boolean{
        boxes[index]!!.forEach {
            if (it.label == label){
                return true
            }
        }
        return false
    }

    fun addLenses(lense: String){
        val label = lense.split("=")[0]
        val len = lense.split("=")[1].toInt()
        val newLens = Lens(label, len)
        val index = hash(label)
        if (index !in boxes){
            boxes[index] = ArrayList<Lens>()
            boxes[index]!!.add(newLens)
        } else if (!contains(label, index)){
            boxes[index]!!.add(newLens)
        }
        else{
            boxes[index]!!.forEach {
                if (it.label == label){
                    it.focalLen = len
                }
            }
        }
    }

    fun removeLenses(label: String){
        val index = hash(label)
        if (index in boxes){
            boxes[index]!!.removeIf { it.label == label }
            if (boxes[index]!!.isEmpty()){
                boxes.remove(index) // not needed, but makes the print look nicer
            }
        }
    }

    fun print(){
        boxes.forEach { it ->
            var lens = ""
            it.value.forEach {len: Lens ->
                lens += "[${len.label} ${len.focalLen}] "
            }
            println("Box ${it.key}:\t$lens")
        }
    }
}
fun main() {
    fun hash(key: String): Int {
        var currVal = 0
        for (ch in key){
            currVal += ch.code
            currVal = (currVal * 17) % 256
        }
        return currVal
    }

    fun part1(input: List<String>): Int {
        val values = input[0].split(",")
        return values.sumOf { hash(it) }
    }

    fun part2(input: List<String>): Int {
        val values = input[0].split(",")
        val boxes = Boxes()
        values.forEach{
//            println("After: $it")
            if ("-" in it){
                boxes.removeLenses(it.split("-")[0])
            } else {
                boxes.addLenses(it)
            }
//            boxes.print()
        }
        return boxes.boxes.map {
            it.value.mapIndexed{ i :Int, len: Lens ->
                (it.key + 1) * (i + 1) * len.focalLen
            }
        }.flatten().sum()
    }

    println("TESTS-----------")
    val testInput = readInput("day15/test_input.txt")
    val test1 = part1(testInput)
    println("Test part 1: $test1")
    check(test1 == 1320)

    val test2 = part2(testInput)
    println("Test part 2: $test2")
    check(test2 == 145)

    println("RUNNING---------")
    val input = readInput("day15/input.txt")
    val part1Sum = part1(input)
    println("Part 1: $part1Sum")

    val part2Sum = part2(input)
    println("Part 2: $part2Sum")
}
