class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}

        ret = []

        '''
        - trick here is that you need to realize that you don't need to do
        any math since the sorted list index technically represents the value of numbers in the array smaller than it if it's not in the dictionary already 
        for example:
            - if 1 not in d: add d[1] = 0 which also happens to be how many numbers are smaller than 1
            - however for a dup number like 2, in the first instance d[2] (value) = 1 (index) and the next time you see the same number, in this case 2, it gets skipped and d[2] = 1 remains the value
        '''
        for k, v in enumerate(temp):
            if v not in d:
                d[v] = k

        for i in nums:
            # looping through nums using the current num as an index in dictionary to get the count of numbers smaller than current one
            # going through the nums list's order and appending will make it so that we're also returning the list in the order of the values passed in
            ret.append(d[i])

        return ret