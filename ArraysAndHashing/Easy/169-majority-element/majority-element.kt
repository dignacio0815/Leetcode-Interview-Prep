class Solution {
    /**
        input 
            nums - array of ints
        return majority element
            majority element reprents some number element that appears more than floor(n/2) times
     */
    fun majorityElement(nums: IntArray): Int {
        val map = mutableMapOf<Int, Int>()

        for (n in nums) {
            map[n] = map.getOrDefault(n, 0) + 1
        }

        val majorityCount = map.size / 2
        var majorityValue = 0
        var key = 0

        for ((k, v) in map) {
            if (majorityCount < v && v > majorityValue) {
                majorityValue = v
                key = k
            }
        }
        
        return key
    }
}