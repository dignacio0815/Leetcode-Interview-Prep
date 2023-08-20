class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return self.constantTime(nums)
        # return self.solutionWithoutFilter(nums)
        # return self.solutionUsingFilter(nums)
        
    def solutionWithoutFilter(self, nums):
        minVal = min(nums)
        maxVal = max(nums)
        
        for n in nums:
            if n < maxVal and n > minVal:
                return n
        return -1
    
    def solutionUsingFilter(self, nums):
        minVal = min(nums)
        maxVal = max(nums)

        try:
            return next(filter(lambda x: x != minVal and x != maxVal, nums))    
        except:
            return -1

    def constantTime(self, nums):
        return sorted(nums[:3])[1] if len(nums) > 2 else -1
        