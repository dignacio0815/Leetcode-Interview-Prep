class Solution {
    fun maxArea(height: IntArray): Int {
        /*
            f(a) = width(left + right) * min(height[left], height[right])
            maxArea = 0
            keep pointers for left, right
            move left pointer +1 if right >
            move right pointer -1 if left is >
            in our case, if =, move left pointer +1
            keep going till i != j
            return maxArea
         */

         var finalMax = 0
         var (l, r) = 0 to height.size - 1
         while (l <= r) {
            var currentMax = (r - l) * minOf(height[l], height[r])
            if (currentMax > finalMax) finalMax = currentMax
            if (height[l] < height[r]) { l+=1 } else { r-=1 }
         }
         return finalMax
    }
}