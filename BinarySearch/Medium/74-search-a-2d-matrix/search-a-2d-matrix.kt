class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        // binary search except with arrays
        // since each array is sorted -- The first integer of each row is greater than the last integer of the previous row.
        // than we can do a binary search on the 2d matrix
        // find the array with the target
        // perform binary search 
        // return true if target found else false
        var targetArr = intArrayOf()
        var l = 0; var r = matrix.size - 1; var m = (l + r) / 2

        // getting target arr
        while (l <= r) {
            // println("${matrix[m][0]..matrix[m][matrix.size]}")
            if (target in matrix[m][0] .. matrix[m][matrix[m].size - 1]) {
                // found the target arr!
                targetArr = matrix[m]
                break
            } else if (target < matrix[m][0]) {
                // move r and m pointers to left side of array
                r = m - 1
                m = (l + r) / 2
            } else if (target > matrix[m][0]) {
                // move l and m pointers to right side of array
                l = m + 1
                m = (l + r) / 2
            }
        }

        // perform binary search on array to verify if target exists
        l = 0; r = targetArr.size - 1; m = (l + r) / 2
        while (l <= r) {
            if (targetArr[m] == target) return true
            else if (target < targetArr[m]) {
                r = m - 1
                m = (l + r) / 2
            } else if (target > targetArr[m]) {
                l = m + 1
                m = (l + r) / 2
            }
        }
        return false
    }
}