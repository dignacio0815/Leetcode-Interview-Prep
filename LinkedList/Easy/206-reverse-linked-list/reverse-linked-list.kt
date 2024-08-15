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
    fun reverseList(head: ListNode?): ListNode? {
        var prev: ListNode? = null
        var cur: ListNode? = head
        var next: ListNode? = head?.next

        while (cur != null) {
            cur?.next = prev
            prev = cur
            cur = next
            next = next?.next
        }

        return prev
    }
}