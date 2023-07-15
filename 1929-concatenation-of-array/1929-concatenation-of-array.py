class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return self.solutionOne(nums)
    
    def solutionOne(self, nums: List[int]) -> List[int]:
        return nums + nums
        
    def solutionTwo(self, nums: List[int]) -> List[int]:
        concatList = []
        for num in nums:
            concatList.append(num)
        
        for num in nums:
            concatList.append(num)
            
        return concatList