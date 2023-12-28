class Solution {
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        /*
            abs implies range (nested loop)

            loop over nums with i:
                loop over i+1 to i + k with j:
                    if nums[i] == nums[j]:
                        found a duplicate within range return true
            return false
         */
         for (i in 0 until nums.size) {
             println("${nums[i]}")
             println()
             for (j in (i + 1) until nums.size) {
                 if (abs(i - j) <= k && nums[i] == nums[j]) {
                     return true
                 } else if (abs(i - j) > k) {
                     break
                 }
             }
         }
         return false
    }
}