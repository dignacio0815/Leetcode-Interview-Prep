class Solution {
    fun intersection(nums1: IntArray, nums2: IntArray): IntArray {
        val set = nums1.toSet()
        val output = mutableSetOf<Int>()
        for (n in nums2) {
            if (n in set) {
                output.add(n)
            }
        }
        return output.toIntArray()
    }
}