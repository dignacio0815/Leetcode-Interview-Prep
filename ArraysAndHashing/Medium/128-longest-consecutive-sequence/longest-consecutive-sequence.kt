class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        val set = nums.toSet()
        var sequenceLength = 0
        
        nums.forEach { n ->
            if (!set.contains(n - 1)) {
                var length = 1
                // check if a sequence is contained in set atm
                while (set.contains(length + n)) {
                    length += 1
                }
                sequenceLength = max(sequenceLength, length)
            }
        }

        return sequenceLength
    }
}