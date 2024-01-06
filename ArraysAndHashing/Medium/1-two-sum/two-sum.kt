class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        // init map to store difference as key and value as index
        // loop through nums
        // if target - current element = a key in map, return value (representing previous index) and current index

        val map = mutableMapOf<Int, Int>()

        nums.forEachIndexed { idx, value -> 
            if (map.containsKey(value)) {
                println(map)
                return intArrayOf(map[value] ?: 0, idx)
            } else {
                map[target - value] = idx
            }
        }

        return intArrayOf(-1, -1)
    }
}