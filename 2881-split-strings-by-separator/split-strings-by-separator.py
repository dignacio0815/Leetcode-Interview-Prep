class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return self.withoutUsingSplit(words, separator)
        arr = []
        for w in words:            
            # append is O(1) vs extend which O(n)
            # decided to use extend since I'd have to loop over the split array either way
            arr.extend(w.split(separator))
            
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
    