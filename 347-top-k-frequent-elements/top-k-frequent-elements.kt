class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val map = mutableMapOf<Int, Int>()
        
        nums.forEach {
            map[it] = map.getOrDefault(it, 0) + 1
        }

        // comparator here is creating a min heap
        val pQueue = PriorityQueue<Int>( compareBy { map[it] } )    

        for ((key, value) in map) {
            pQueue.offer(key)
            if (pQueue.size > k) pQueue.poll()
        }

        println(pQueue)
        return pQueue.toIntArray()
    }
}