class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return self.solutionOne(n)

    def yieldDigit(self, num: int) -> int: 
        while (num > 0):
            digit = num % 10
            yield digit
            num = num // 10
            
    def solutionOne(self, num: int) -> int:
        product = 1
        sum = 0
        
        for digit in self.yieldDigit(num):
            product *= digit
            sum += digit
            
        return product - sum
        
    def solutionTwo(self, num: int) -> int:
        product = 1
        sum = 0
        while n > 0:
            temp = n % 10
            product *= temp
            sum += temp
            n = n // 10
        
        return product - sum