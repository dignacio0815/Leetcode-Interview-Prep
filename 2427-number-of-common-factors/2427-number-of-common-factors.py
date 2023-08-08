class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return self.bruteForce(a, b)   
    
    def bruteForce(self, a: int, b: int) -> int:
        if (a > b):
            return self.countFactors(a, b)
        else:
            return self.countFactors(b, a)
    
    def countFactors(self, a, b):
        count = 0
        for i in range(1, a + 1):
            if (a % i == 0 and b % i == 0):
                count += 1
        return count