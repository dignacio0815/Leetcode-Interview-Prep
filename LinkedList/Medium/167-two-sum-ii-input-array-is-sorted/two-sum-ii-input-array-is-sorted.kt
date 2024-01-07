class Solution {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        // init pointers i = 0 ; j = length - 1
        var i = 0; var j = numbers.size - 1

        while (i < j) {
            // implies that the sum is greater so we need to move down j
            if (numbers[i] + numbers[j] > target) {
                j -= 1
            } else if (numbers[i] + numbers[j] < target) {
                // implies that the sum is less than targer so we need to move up i
                i += 1
            } else {
                return intArrayOf(i+1, j+1)
            }
        }
        
        // in case no solution return default [-1, -1]
        return intArrayOf(-1, -1)
    }
}