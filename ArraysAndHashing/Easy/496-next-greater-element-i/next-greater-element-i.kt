class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        val list: MutableList<Int> = mutableListOf()

        for (i in 0 until nums1.size) {
            var flag = false
            for (j in 0 until nums2.size) {
                if (nums1[i] == nums2[j]) {
                    for (k in j + 1 until nums2.size) {
                        if (nums2[k] > nums2[j]) {
                            list.add(nums2[k])
                            flag = true
                            break
                        }
                    }
                }
            }
            if (!flag) {
                list.add(-1)
            }
        }

        return list.toIntArray() 
    }
}