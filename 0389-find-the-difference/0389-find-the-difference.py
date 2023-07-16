class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        for idx in range(len(s)):
            if (s[idx] != t[idx]):
                return t[idx]
        
        return t[-1]