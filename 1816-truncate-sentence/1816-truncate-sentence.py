class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return self.bruteForce(s, k)
    
    def bruteForce(self, s: str, k: int) -> str:
        splitStr = s.split(" ")
        return (" ").join(splitStr[0:k])
            

        

            