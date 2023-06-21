class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        anagrams = []
        
        for s in strs:
            # print(''.join(sorted(s)))
            # print(s)
            temp = ''.join(sorted(s))
            if temp in hashMap:
                hashMap[temp].append(s)
            else:
                hashMap[temp] = [s]
                
        # print(hashMap)
        
        for (k,v) in hashMap.items():
            anagrams.append(v)
        return anagrams
