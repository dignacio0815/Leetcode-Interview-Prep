class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        // init map
        val map = mutableMapOf<String, MutableList<String>>()
        val list = mutableListOf<List<String>>()
        for (s in strs) {
            // if the anagram already exists in map
            val sortedStr = s.toCharArray().sorted().joinToString("")
            if (map.containsKey(sortedStr)) {
                map[sortedStr]?.add(s)
            } else {
                // doesn't exist, than we add a new key val into map
                map[sortedStr] = mutableListOf(s)
            }
        }

        for ((k, v) in map) {
            list.add(v)
        }

        return list
    }
}