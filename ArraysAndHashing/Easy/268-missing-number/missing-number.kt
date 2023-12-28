class Solution {
    fun missingNumber(nums: IntArray): Int {
        /*
            sort nums
            loop through nums 
                if current element doesn't equal next element - 1 return
            return either nums[size - 1] + 1 (in case missing element is at end)
            return 0 if missing element is at start
         */

        // brute force using sorting
        // nums.sort()
        // for (i in 0 until nums.size - 1) {
        //     if (nums[i] != nums[i + 1] - 1) {
        //         return nums[i + 1] - 1
        //     }
        // }
         
        // return if (nums[0] == 0) nums[nums.size - 1] + 1 else 0

        // optimal approach using addition and subtraction
        var numsSum = 0
        var finalSum = 0

        for (n in nums) {
            numsSum += n
        }

        for (n in 1..nums.size) {
            finalSum += n
        }

        return finalSum - numsSum
    }
}