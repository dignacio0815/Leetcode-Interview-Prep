class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var l = 0; var r = nums.size - 1; var m = (l + r) / 2

        while (l <= r) {
            println("l $l, r $r, m $m")
            if (nums[m] == target) return m
            else if (target < nums[m]) {
                // target is on left side of array
                r = m - 1
                m = (l + r) / 2
            } else if (target > nums[m]) {
                // target is on right side of array
                l = m + 1
                m = (l + r) / 2
            }
        }

        return -1
    }
}