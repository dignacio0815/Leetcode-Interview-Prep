'''
time: O(n) because algo has to loop over entire list of string and add to hashMap
space: O(n) because 
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in hashMap:
                hashMap[temp].append(s)
            else:
                hashMap[temp] = [s]
            
        return hashMap.values()
