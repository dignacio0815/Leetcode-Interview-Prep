class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return self.solutionTwo(sentences)
        
    def solutionOne(self, sentences: List[str]) -> int:
        maxVal = float('-inf')
        for word in sentences: 
            curWord = word.split(' ')
            if (len(curWord) > maxVal):
                maxVal = len(curWord)
        return maxVal
    
    def solutionTwo(self, sentences: List[str]) -> int:
        wordCount = 0
        for word in sentences:
            tempCount = 1
            for letter in word:
                if letter == " ":
                    tempCount += 1
            if (tempCount > wordCount):
                wordCount = tempCount
        return wordCount