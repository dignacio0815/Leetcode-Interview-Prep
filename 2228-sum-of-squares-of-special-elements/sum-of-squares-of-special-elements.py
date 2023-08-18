class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        squareSum = 0
        
        for idx, val in enumerate(nums):
            if len(nums) % (idx + 1) == 0:
                squareSum += (val * val)
                
        return squareSum
                
