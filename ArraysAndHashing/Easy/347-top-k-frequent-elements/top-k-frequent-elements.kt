class Solution {
    /*
        init a map to store key (element) and value (count of elements seen)
        loop through nums to get count of elements - store in map
        return filter map for pairs whose value >= k
    */        

    fun topKFrequent(nums: IntArray, k: Int): MutableList<Int> {
        val map = mutableMapOf<Int, Int>()

        for (n in nums) {
            map[n] = map.getOrDefault(n, 0) + 1
        }

        val result = map.entries
            .sortedByDescending { it.value }
            .slice(0..k-1)
            .map { it.key }
            .toMutableList()
            
        return result
    }
}

