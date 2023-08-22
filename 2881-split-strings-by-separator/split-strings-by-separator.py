class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return self.withoutUsingSplit(words, separator)
        
    def withoutUsingSplit(self, words: List[str], separator: str) -> List[str]:
        arr = []
        for w in words:
            w += separator
            stringBuilder = ""
            for idx in range(len(w)):
                if w[idx] != separator:
                    stringBuilder += w[idx]
                else:
                    arr.append(stringBuilder)
                    stringBuilder = ""
        return [w for w in arr if w != ""]
    
    def solutionWithSplit(self, words: List[str], separator: str) -> List[str]:
        arr = []
        tempArr = separator.join(words).split(separator)
        for w in tempArr:
            if w != "":
                arr.append(w)
        return arr