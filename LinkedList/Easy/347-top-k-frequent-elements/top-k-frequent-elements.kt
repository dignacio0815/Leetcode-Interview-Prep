class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        // init map
        val map = mutableMapOf<Int,Int>()
        // init priority queue min heap
        val pQueue = PriorityQueue<Int>( compareBy { map[it] } )

        // creating frequency count for each num
        nums.forEach {
            map[it] = map.getOrDefault(it, 0) + 1
        }

        map.forEach { key, _ ->
            // inserting into heap
            pQueue.offer(key)
            // if queue size > k, than remove pop current item in queue
            // this works because its a min heap implying elements with lowest frequency
            // are at start of queue
            if (pQueue.size > k) pQueue.poll()
        }

        return pQueue.toIntArray()
    }
}