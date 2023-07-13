class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return self.trivialSolution(sentences)
        
    def trivialSolution(self, sentences: List[str]) -> int:
        maxVal = float('-inf')
        for word in sentences: 
            curWord = word.split(' ')
            if (len(curWord) > maxVal):
                maxVal = len(curWord)
        return maxVal