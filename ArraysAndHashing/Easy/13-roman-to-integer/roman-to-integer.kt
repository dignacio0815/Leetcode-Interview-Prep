class Solution {
    fun romanToInt(s: String): Int {
        // init map containing roman to int values
        val map = mapOf(
            'I' to 1,
            'V' to 5,
            'X' to 10,
            'L' to 50,
            'C' to 100,
            'D' to 500,
            'M' to 1000
        )
        var count = 0

        // loop through string s
        // check for current element is either I, X, or C, we subtract 
        // always add the element

        for (i in 0..s.length - 2) {
            if (s[i] == 'I' && (s[i + 1] == 'V' || s[i + 1] == 'X')) {
                // subtracting by 1
                count -= map[s[i]] ?: 0
            } else if (s[i] == 'X' && (s[i + 1] == 'L' || s[i + 1] == 'C')) {
                // subtracting by 10
                count -= map[s[i]] ?: 0
            } else if (s[i] == 'C' && (s[i + 1] == 'D' || s[i + 1] == 'M')) {
                // subtracting by 100
                count -= map[s[i]] ?: 0
            } else {
                count += map[s[i]] ?: 0
            }
        }
        count += map[s[s.length - 1]] ?: 0
        return count
    }
}