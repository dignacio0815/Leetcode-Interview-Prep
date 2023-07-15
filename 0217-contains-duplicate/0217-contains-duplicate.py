'''
resources: https://www.geeksforgeeks.org/set-add-python/
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.solutionOne(nums)
        
    def solutionOne(self, nums: List[int]) -> bool:
        dupsSet = set()
        for num in nums:
            print(num)
            if num in dupsSet:
                return True
            dupsSet.add(num)
        return False