class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        currentMax = 1
        runningMax = 0
        index = 0
        if len(nums) < 1:
            return 0

        for x in s:
            runningMax = 0
            if x - 1 not in s:
                runningMax = 1
                cur = x
                while cur + 1 in s:
                    runningMax += 1
                    cur += 1
                currentMax = max(currentMax, runningMax)
        
        return currentMax

# [0,1,2,3,6,7,8,9,10]        
            


        

"""
unsorted -- binary search, potentially can't do 2 pointers??
must run in O(n)
cant sort because that becomes O(n log n)

[100,4,200,1,3,2]

put all numbers in a set

loop through it and see if num - 1 or + 1 in set, if not, keep track of new max

return count
"""