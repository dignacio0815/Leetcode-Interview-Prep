class Solution {
    fun missingNumber(nums: IntArray): Int {
        /*
            init set to hold nums
            loop through nums 
                if current element not in set, return
            return default number
         */

        nums.sort()
        for (i in 0 until nums.size - 1) {
            if (nums[i] != nums[i + 1] - 1) {
                return nums[i + 1] - 1
            }
        }
         
        return if (nums[0] == 0) nums[nums.size - 1] + 1 else 0
        
    }
}