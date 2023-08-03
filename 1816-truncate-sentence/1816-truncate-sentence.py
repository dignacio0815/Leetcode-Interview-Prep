class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return self.optimal(s, k)
        return self.bruteForce(s, k)
    
    def bruteForce(self, s: str, k: int) -> str:
        splitStr = s.split(" ")
        return (" ").join(splitStr[0:k])

    def optimal(self, s: str, k: int) -> str:
        for i, l in enumerate(s):
            if (k == 0):
                return s[0:i - 1]
            if (l == ' '):
                k -= 1
            
        return s
            

        

            