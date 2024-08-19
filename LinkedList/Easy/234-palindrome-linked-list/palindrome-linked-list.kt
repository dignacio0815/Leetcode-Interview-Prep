/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun isPalindrome(head: ListNode?): Boolean {
        return bruteForce(head)
    }

    fun bruteForce(head:ListNode?): Boolean {
        val list = mutableListOf<ListNode?>()

        var ptr = head
        while (ptr != null) {
            list.add(ptr)
            ptr = ptr?.next
        }

        var i = 0
        var j = list.size - 1
        while (i < j) {
            if (list[i]?.`val` != list[j]?.`val`) {return false}
            i+=1
            j-=1
        }

        return true
    }
}