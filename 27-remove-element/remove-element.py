class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while (i <= j):
            # if i == val, go to j and find spot != val and swap, move up / down i and j respectively
            if (nums[i] == val):
                if (nums[j] != val): # swap the elements
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                elif (nums[j] == val):
                    j -= 1
            elif (nums[i] != val):
                i+=1
        return i