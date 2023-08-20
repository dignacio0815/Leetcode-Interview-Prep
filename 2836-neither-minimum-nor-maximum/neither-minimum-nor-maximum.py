class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minVal = min(nums)
        maxVal = max(nums)
        
        temp = minVal
        
        for n in nums:
            if n < maxVal and n > minVal:
                temp = n
        if minVal == temp or maxVal == temp:
            return -1
        return temp