class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
         // sorting solution
        sortingSolution(nums1, m, nums2, n)
        println(nums1.contentToString())
    }

    // Time O(n * log n)
    // Space O(1)
    fun sortingSolution(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        nums2.copyInto(nums1, nums1.size - n, 0, n)
        nums1.sort()
    }
}