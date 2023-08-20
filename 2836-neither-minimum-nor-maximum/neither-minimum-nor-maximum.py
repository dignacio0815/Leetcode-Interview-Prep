class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return self.solutionUsingFilter(nums)
        minVal = min(nums)
        maxVal = max(nums)
        temp = minVal
        
        for n in nums:
            if n < maxVal and n > minVal:
                temp = n
        if minVal == temp or maxVal == temp:
            return -1
        return temp
    
        
        
    def solutionUsingFilter(self, nums):
        minVal = min(nums)
        maxVal = max(nums)

        for x in filter(lambda x: x != minVal and x != maxVal, nums):
            return x
        return -1
