class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        // create prefix and suffix products 
        // loop through nums and multiply prefix[i-1] and suffix[i+1] values for current product
        // if i - 1 or i + 1 out of bounds, multiply by 1
        
        val prefix = MutableList<Int>(nums.size) {0}
        val suffix = MutableList<Int>(nums.size) {0}
        val products = IntArray(nums.size) {0}
        var product = 1

        // calculate product for prefix list
        nums.forEachIndexed { idx, num -> 
            product *= num
            prefix[idx] = product
        }

        // reset product to 1
        product = 1
        
        // calculate product for suffix list
        nums.toMutableList().asReversed().forEachIndexed { idx, num -> 
            product *= num
            suffix[nums.size - 1 - idx] = product
        }

        // calculate product current element which is prefix[i-1] * suffix[i+1] values for current product
        nums.forEachIndexed { idx, value -> 
            if (idx == 0) {
                product = 1 * suffix[idx + 1]
            } else if (idx == nums.size - 1) {
                product = 1 * prefix[idx - 1]
            } else {
                product = suffix[idx + 1] * prefix[idx - 1]
            }
            products[idx] = product
        }

        return products
    }
}