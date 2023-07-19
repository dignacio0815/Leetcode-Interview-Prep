class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if (self.isPalindrome(word)):
                return word
        return ""
    
    def isPalindrome(self, word: str) -> bool:
        # loop over only half of the string to determine if string is palindromic
        # if word at current doesn't equal opposite index, than return false else true
        for i in range(len(word) // 2):
            if (word[i] != word[-1 - i]):
                return False
        return True
    
            