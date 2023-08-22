class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return self.solutionWithSplit(words, separator)
        
    def withoutUsingSplit(self, words: List[str], separator: str) -> List[str]:
        arr = []
        for w in words:
            stringBuilder = ""
            print(w)
            for idx in range(len(w)):
                if w[idx] != separator:
                    stringBuilder += w[idx]
                elif w[idx] == separator:
                    if (stringBuilder != ""):
                        arr.append(stringBuilder)
                    stringBuilder = ""
            if (stringBuilder != ""):
                arr.append(stringBuilder)
        return arr
    
    def solutionWithSplit(self, words: List[str], separator: str) -> List[str]:
        arr = []
        tempArr = separator.join(words).split(separator)
        for w in tempArr:
            if w != "":
                arr.append(w)
        return arr