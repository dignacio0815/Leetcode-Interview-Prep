class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        // init set
        val set = nums.toSet()
        var sequenceLength = 0
        
        nums.forEach { n ->
            // if set doesn't contain the previous number, this implies the start of a new sequence
            if (!set.contains(n - 1)) {
                // length to be added to n is 1 because a sequence is reprsented as [n, n + 1, n + 2, n + n ...]
                var length = 1
                // check if a sequence is contained in set atm
                while (set.contains(length + n)) {
                    // if the set contains this n + length number, than increment the length
                    length += 1
                } 
                // we only care about max length so when while loop is done either get the new max length or continue
                sequenceLength = max(sequenceLength, length)
            }
        }

        return sequenceLength
    }
}