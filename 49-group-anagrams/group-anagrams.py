from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        sets = defaultdict(list)
        sortedList = [''.join(sorted(s)) for s in strs]
        
        for i, v in enumerate(sortedList):
            sets[v].append(strs[i])

        return list(sets.values())
"""
create a list for each grouping of anagrams

if empty, return empty string nested list

loop through list and compare each word to current one and see if the letters match current one via set operation
    if yes, insert to match list
    else move on to next word
"""