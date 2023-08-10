class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # return self.usingLoop(num)
        return self.usingRegex(num)
    
    def usingLoop(self, num: str) -> str:
        i = len(num) - 1
        while i > -1:
            if num[i] != '0':
                break
            else:
                i -= 1
        return num[0:i + 1]
    
    def usingRegex(self, num: str) -> str:
        return re.sub(r'0+$', '', num)
