class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if (p == ')' and stack and stack[-1] == '('):
                stack.pop()
            elif (p == ']' and stack and stack[-1] == '['):
                stack.pop()
            elif (p == '}' and stack and stack[-1] == '{'):
                stack.pop()
            else:
                stack.append(p)
        return not stack