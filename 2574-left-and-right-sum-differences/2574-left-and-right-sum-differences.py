class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return self.runningSum(nums)
    
    def runningSum(self, nums: List[int]) -> List[int]:
        left, right = [0] * len(nums), [0] * len(nums)
        total = 0
        
        for i in range(1, len(nums)):
            total += nums[i-1]
            left[i] = total
        
        # reset counter to 0
        total = 0
        
        for i in reversed(range(len(nums))):
            if (i == 0):
                break
            total += nums[i]
            right[i - 1] = total
        
        for i, val in enumerate(left):
            left[i] = abs(val - right[i])
                
        return left