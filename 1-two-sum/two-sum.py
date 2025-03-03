class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, v in enumerate(nums):

            diff = target - v

            if (v in map):
                return [i, map[v]]

            map[diff] = i

        return [0,1]