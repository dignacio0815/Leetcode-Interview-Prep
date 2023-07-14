class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # return self.solutionOne(jewels, stones)
        # return self.solutionTwo(jewels, stones)
        return self.solutionThree(jewels, stones)
        
    def solutionOne(self, jewels: str, stones: str) -> int:
        jewelCount = 0
        
        for j in jewels:
            for s in stones:
                if j == s:
                    jewelCount += 1
                    
        return jewelCount
    
    def solutionTwo(self, jewels: str, stones: str) -> int:
        jewelMap = {}
        
        for j in jewels:
            # no need to check for duplicate keys since jewels are UNIQUE
            jewelMap[j] = 0
            
        for s in stones:
            if s in jewelMap:
                jewelMap[s] += 1
        
        return sum(jewelMap.values())
    
    def solutionThree(self, jewels: str, stones: str) -> int:
        jewelSet = set(jewels)
        jewelCount = 0
        
        for s in stones:
            if s in jewelSet:
                jewelCount += 1
                
        return jewelCount