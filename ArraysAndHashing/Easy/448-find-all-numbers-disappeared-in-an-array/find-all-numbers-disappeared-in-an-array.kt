class Solution {
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        val list: MutableList<Int> = MutableList(nums.size) { 0 }
        val output = mutableListOf<Int>()

        nums.forEach {
            list[it - 1] = list[it - 1] + 1 ?: 1
        }

        list.forEachIndexed { index, `val` ->
            if (`val` == 0) {
                output.add(index + 1)   
            }
        }

        return output
    }
}