class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return self.bruteForce(nums)
        
    def bruteForce(self, nums: List[int]) -> int:
        pairs = 0
        for j in range(len(nums)):
            for i in range(j):
                if (nums[i] == nums[j]):
                    pairs+=1
        return pairs
        
    def usingMap(self, nums: List[int]) -> int:
        pairs = 0
        
        freq = {}
        
        for n in nums:
            if (n in freq):
                pairs += freq[n]
                freq[n] += 1
            else:
                freq[n] = 1                                                                                                                                         
        return pairs
    