class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        // sorting, hashing, bruteforce
        // val alphabet = HashMap<Char, Int>()
        val alphabet = mutableMapOf<Char, Int>()
        // Add the alphabet to the hashmap
        for (ch in 'a'..'z') {
            alphabet[ch] = 0
        }

        // loop through s and t and add / subtract their letters
        for (l in s) {
            alphabet[l] = (alphabet[l] ?: 0) + 1
        }

        for (l in t) {
           alphabet[l] = (alphabet[l] ?: 0) - 1
        }

        for ((key, value) in alphabet) {
            if (value != 0) {
                return false
            }
        }

        return true
    }
}