from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        l = []
        for n in nums:
            d[n] += 1

        while k > 0:
            maxVal = max(d.items(), key=lambda x: x[1])
            l.append(maxVal[0])
            d.pop(maxVal[0])
            k -= 1
        
        return l 
"""
given k, return k most frequent meaning give the numbers in the list that appear the most times but only the top "k" numbers

so for example, if you had [1,2,3,3,4,4,4] k = 2 --> [3,4] 

since 3 and 4 are the most frequent numbers followed by 1 and 2

create a dict that loops through nums
    counts occurences

create a set to hold k frequent ints

while k > 0:
    grab max from dict store key
    pop (key, value) from dict

return list
"""        