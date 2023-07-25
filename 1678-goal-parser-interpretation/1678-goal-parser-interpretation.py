import re

class Solution:
    def interpret(self, command: str) -> str:
        parser = ""
        for i, val in enumerate(command):
            if (command[i] == '(' and command[i+1] == ')'):
                parser += 'o'
            elif (command[i].isalpha()):
                parser += command[i]
        return parser
        
    def regex(self, command: str) -> str:
        return re.sub(r'\(\)','o',re.sub(r'\(al\)','al',command))