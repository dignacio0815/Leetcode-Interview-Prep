class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var k = 0
        var left = 0
        var right = nums.size - 1

        while (left <= right) {
            // case where left pointer doesn't equal val
            if (nums[left] != `val`) {
                k += 1
                left += 1
            }

            // case where left pointer equals val
            else if (nums[left] == `val`) {
                if (nums[right] != `val`) {
                    val temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp 
                    left += 1
                    right -= 1
                    k += 1
                } else if (nums[right] == `val`) {
                    right -= 1
                }
            } 
        }

        return k   
    }
}