class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return self.withoutUsingSplit(words, separator)
     
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
    