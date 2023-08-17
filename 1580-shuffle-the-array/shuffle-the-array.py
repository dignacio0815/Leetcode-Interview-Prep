class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return self.solutionWithYield(nums, n)
        # return self.solutionWithForLoop(nums, n)
    
    def solutionWithForLoop(self, nums: List[int], n: int) -> List[int]:
        l = []
        for i in range(0, n):
            l.extend([nums[i], nums[i + n]])
        return l
    
    # function that feeds the indexes
    def solutionWithYield(self, nums: List[int], n: int) -> List[int]:
        l = []
        
        return [nums[i] for i in self.yieldIndexes(n)]
        
    def yieldIndexes(self, n):
        for i in range(0, n):
            yield i
            yield i + n
    