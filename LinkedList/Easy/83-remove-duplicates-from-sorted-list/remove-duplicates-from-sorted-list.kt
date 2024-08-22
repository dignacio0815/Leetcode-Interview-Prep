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
        /*
            loop while head.next
                if equals
                    head?.next = head?.next?.next
                does not equals
                    head = head?.next
            return head
         */

         var h: ListNode? = head

         while (h?.next != null) {
            if (h.`val` == h.next.`val`) {
                h?.next = h?.next?.next
            } else {
                h = h?.next
            }
         }
        return head
    }
}