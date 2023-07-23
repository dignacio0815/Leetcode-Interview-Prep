class Solution:
    def defangIPaddr(self, address: str) -> str:
        defangedAddress = ""
        for i, val in enumerate(address):
            if (val == '.'):
                defangedAddress += "[.]"
            else:
                defangedAddress += val
        return defangedAddress