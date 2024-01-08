class Solution {
    fun maxArea(height: IntArray): Int {
        var i = 0; var j = height.size - 1
        var area = 0
        
        while (i < j) {
            var currentArea = min(height[i], height[j]) * (j - i)
            area = max(area, currentArea)
            if (height[i] < height[j]) {
                i += 1
            } else if (height[j] < height[i]) {
                j -= 1
            } else {
                i+=1
                j-=1
            }
        }

        return area
    }
}