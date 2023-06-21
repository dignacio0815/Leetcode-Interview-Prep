'''
time: O(n log n) because algo has to loop over entire list of string and add to hashMap but also sorts the entire string when comparing
space: O(n) because algo stores n number of unique anagrams as keys in hashMap
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
