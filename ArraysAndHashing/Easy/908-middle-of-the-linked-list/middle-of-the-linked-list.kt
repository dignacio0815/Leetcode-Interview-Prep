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
    fun middleNode(head: ListNode?): ListNode? {
        var slowNode: ListNode? = head
        var fastNode: ListNode? = head?.next
        while(fastNode != null) {
            slowNode = slowNode?.next
            fastNode = fastNode?.next?.next
        }

        return slowNode
    }
}