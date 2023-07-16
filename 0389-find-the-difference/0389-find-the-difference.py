'''
resource links:
- https://www.programiz.com/python-programming/methods/built-in/enumerate
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        for idx, letter in enumerate(s):
            if (s[idx] != t[idx]):
                return t[idx]
        
        return t[-1]        