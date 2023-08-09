class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = [0] * 26
        # ascii lowercase alphabet a-z = 97-122
        for l in s:
            letters[ord(l.lower()) - ord('a')] += 1
        
        for l in t:
            letters[ord(l.lower()) - ord('a')] -= 1
                
        for idx, val in enumerate(letters):
            if val != 0:
                return chr(idx + ord('a'))
            
        return chr(ord('a'))