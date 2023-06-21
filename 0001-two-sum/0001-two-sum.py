'''
time: O(n) because algo loops over n number of element based on size of array
space: O(n) because algo holds onto dictionary of n number of elements dependent on size of array
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for index in range(len(nums)):
            x = target - nums[index]
            if x in hashMap:
                return [index, hashMap[x]]
            else:
                hashMap[nums[index]] = index
        return [0,1]
    
    