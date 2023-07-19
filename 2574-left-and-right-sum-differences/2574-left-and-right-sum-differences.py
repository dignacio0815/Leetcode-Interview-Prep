class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return self.runningSum(nums)
    
    def runningSum(self, nums: List[int]) -> List[int]:
        # init arrays size of nums to 0
        left, right = [0] * len(nums), [0] * len(nums)
        # total to keep track of running sum in left and right arrays
        total = 0
        
        # calculate running sum from left to right
        for i in range(1, len(nums)):
            total += nums[i-1]
            left[i] = total
        
        # reset total to 0 since we're looping over right to left now 
        total = 0
        
        # calculate running sum from right to left
        for i in reversed(range(len(nums))):
            # if index is 0, we can break out of loop
            if (i == 0):
                break
            total += nums[i]
            right[i - 1] = total
        
        # find abs val of left - right 
        # note either right or left array could've been used here
        for i, val in enumerate(left):
            left[i] = abs(val - right[i])
                
        return left