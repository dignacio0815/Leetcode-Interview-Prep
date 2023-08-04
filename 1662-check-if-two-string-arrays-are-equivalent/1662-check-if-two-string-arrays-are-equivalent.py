class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return self.usingStrings(word1, word2)
    
    def usingStrings(self, word1: List[str], word2: List[str]) -> bool:
        str1, str2 = "", ""
        
        for i, _ in enumerate(word1):
            str1 += word1[i]
            
        for i, _ in enumerate(word2):
            str2 += word2[i]
            
        return str1 == str2