class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var k = 1
        var left = 0
        var right = left + 1

        while (right < nums.size) {
            if (nums[left] == nums[right]) {
                right++
            } else if (nums[left] != nums[right]) {
                nums[left + 1] = nums[right]
                left++
                k++
            }
        }
        return k
    }
}