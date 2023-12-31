class Solution {
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        val list: MutableList<Int> = MutableList(nums.size) { 0 }
        val output = mutableListOf<Int>()

        nums.forEach {
            // println(it)
            // println(it - 1)
            // println()
            list[it - 1] = list[it - 1] + 1 ?: 1
        }

        println(list)

        list.forEachIndexed { index, `val` ->
            if (`val` == 0) {
                output.add(index + 1)   
            }
        }
        
        println(output)
        return output
    }
}