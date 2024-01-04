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
    fun deleteDuplicates(head: ListNode?): ListNode? {
        var currentNode: ListNode? = head
        var nextNode: ListNode? = head?.next
        while (currentNode != null) {
            // check if current node still equals next node
            while (currentNode?.`val` == nextNode?.`val`) {
                nextNode = nextNode?.next
            }
            currentNode?.next = nextNode
            currentNode = currentNode?.next
            nextNode = currentNode?.next
        }

        return head
    }
}