class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return self.solutionOne(nums)
    
    def solutionOne(self, nums: List[int]) -> List[int]:
        return nums + nums
        