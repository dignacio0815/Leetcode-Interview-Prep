class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return self.runningSum(nums)
    
    def runningSum(self, nums: List[int]) -> List[int]:
        diffArr = []
        left, right = 0, 0
        for i in range(0, len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            diffArr.append(abs(left - right))
            
        return diffArr