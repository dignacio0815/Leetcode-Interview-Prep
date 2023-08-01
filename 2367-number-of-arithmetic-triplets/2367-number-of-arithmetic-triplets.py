class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        s = set(nums) 
        for n in nums:
            if (n - diff in s and n + diff in s):
                count += 1
        return count