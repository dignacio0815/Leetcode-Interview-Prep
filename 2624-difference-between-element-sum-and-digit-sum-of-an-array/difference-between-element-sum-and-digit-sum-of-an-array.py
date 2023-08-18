class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(self.getElementSum(nums) - self.getDigitSum(nums))
        
    def getElementSum(self, nums: List[int]) -> int:
        elementSum = 0
        for e in nums:
            elementSum += e
        return elementSum
    
    def getDigitSum(self, nums: List[int]) -> int:
        digitSum = 0
        for n in nums: 
            digitSum += self.getDigits(n)
        
        return digitSum
        
    def getDigits(self, num: int) -> int:
        digitSum = 0
        while num > 0:
            digitSum += num % 10
            num = num // 10
        return digitSum