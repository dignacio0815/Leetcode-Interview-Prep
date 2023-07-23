class Solution:
    def defangIPaddr(self, address: str) -> str:
        return self.solutionTwo(address)

    def solutionOne(self, address: str) -> str:
        defangedAddress = ""
        for i, val in enumerate(address):
            if (val == '.'):
                defangedAddress += "[.]"
            else:
                defangedAddress += val
        return defangedAddress
    
    def solutionTwo(self, address: str) -> str:
        return "[.]".join(address.split("."))