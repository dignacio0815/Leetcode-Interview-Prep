'''
notes:
- 0 indexed array with distinct strings
- pairs are classified as words[i] == reverse(words[j]) where 0 <= i < j < words.length
'''
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        return self.solutionWithSet(words)

    def solutionWithNestForLoop(self, words: List[str]) -> int:
        numPairs = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1]:
                    numPairs += 1
                    break
        return numPairs
    
    def solutionWithSet(self, words: List[str]) -> int:
        pairsSet = set()
        numPairs = 0

        for w in words:
            if w[::-1] in pairsSet:
                numPairs += 1
            else:
                pairsSet.add(w)
        
        return numPairs