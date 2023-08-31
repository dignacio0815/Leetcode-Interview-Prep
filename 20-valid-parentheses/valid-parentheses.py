class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for paren in s:
            if paren is '(' or paren is '[' or paren is '{':
                stack.append(paren)
            
            elif stack and paren is ')' and stack[-1] is '(':
                stack.pop()

            elif stack and paren is ']' and stack[-1] is '[':
                stack.pop()

            elif stack and paren is '}' and stack[-1] is '{':
                stack.pop()
            
            else:
                stack.append(paren)
        
        return not stack