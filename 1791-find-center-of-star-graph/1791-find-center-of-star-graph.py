class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # return self.solutionOne(edges)
        return self.solutionTwo(edges)
        
    def solutionTwo(self, edges: List[List[int]]) -> int:
        s = set()
        
        for e in edges:
            if (e[0] in s):
                return e[0]
            elif (e[1] in s):
                return e[1]
            else:
                s.update([e[0], e[1]])
        # default case                
        return e[0][0]
    
    def solutionTwo(self, edges: List[List[int]]) -> int:
        firstVal = edges[0][0]
        secondVal = edges[0][1]
        
        if (edges[1][0] == firstVal or edges[1][1] == firstVal):
            return firstVal
        else:
            return secondVal