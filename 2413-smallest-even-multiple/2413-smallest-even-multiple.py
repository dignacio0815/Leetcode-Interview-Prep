'''
P -> single int 
r -> return back smallest multiple as an int
e -> given n = 5, S.E.M. is 10 
p -> 
'''
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return self.optimalSolution(n)
        
    def bruteForce(self, n: int) -> int:
        flag = True
        num = 1
        while flag:
            if (num % 2 == 0 and num % n == 0):
                flag = False
                return num
            else:
                num += 1
        return -1
    
    def optimalSolution(self, n: int) -> int:
        return (n * 2) if (n % 2 == 1) else n
