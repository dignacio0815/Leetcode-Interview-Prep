class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressedList = []
        for i in range(0, len(nums), 2):
            decompressedList.extend([nums[i+1]] * nums[i])
        return decompressedList