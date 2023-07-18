'''
p - array (nums)
r - list representing the running sum
e - [1,2,3,4] returns [1,3,6,10]
p -  
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return self.runningSumInPlaceArr(nums)
    
    def runningSumUsingList(self, nums: List[int]) -> List[int]:
        runningSumArr = []
        currentSum = 0
        
        for num in nums:
            currentSum += num
            runningSumArr.append(currentSum)
            
        return runningSumArr
    
    def runningSumInPlaceArr(self, nums: List[int]) -> List[int]:
        for idx in range(1, len(nums)):
            nums[idx] = nums[idx] + nums[idx - 1]
        return nums                