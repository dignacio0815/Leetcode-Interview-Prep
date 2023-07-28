class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return self.buildArrayWithNewArr(nums)
    
    def buildArrayWithNewArr(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i, v in enumerate(nums):
            arr[i] = nums[nums[i]]
        return arr
    
    def oneLiner(self, nums: List[int]) -> List[int]:
        return [nums[v] for i, v in enumerate(nums)]