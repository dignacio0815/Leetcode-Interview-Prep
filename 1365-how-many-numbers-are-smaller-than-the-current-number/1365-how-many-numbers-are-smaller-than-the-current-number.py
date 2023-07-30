class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return self.bruteForce(nums)
        
    def bruteForce(self,  nums):
        arr = []
        for i, x in enumerate(nums):
            counter = 0
            for j, y in enumerate(nums):
                if i != j and x > y:
                    counter += 1
            arr.append(counter)
        return arr