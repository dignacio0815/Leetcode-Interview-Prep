class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return self.usingSplit(words, separator)
     
    def usingSplit(self, words: List[str], separator: str) -> List[str]:
        arr = []
        for w in words:
            tempArr = w.split(separator)
            for i in tempArr:
                if i != "":
                    arr.append(i)
        return arr
        
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
    