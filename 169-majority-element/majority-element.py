class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = 0
        freq = {}
        
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            
        
        for key, val in freq.items():
            if val > (len(nums) // 2) and val > majorityElement:
                majorityElement = key                
        
        return majorityElement