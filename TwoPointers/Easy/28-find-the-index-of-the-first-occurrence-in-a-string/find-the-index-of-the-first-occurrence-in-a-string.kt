class Solution {
    fun strStr(haystack: String, needle: String): Int {
        for (i in 0 .. haystack.length - needle.length) {
            if (haystack.slice(i until i + needle.length) == needle) {
                return i
            }
        }
        return -1
    }
}