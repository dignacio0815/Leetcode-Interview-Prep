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
    fun removeElements(head: ListNode?, `val`: Int): ListNode? {
        /*
        keep track of prev, cur, and next
        loop through linked list while cur != null
            if curr.val == val:
                remove this node 
                point prev to the next node 
                cur = next
                next = cur.next
            else:
                move prev, cur, and next up by 1
        return head
         */

        var newHead = head
        var prev: ListNode? = null
        var cur: ListNode? = head
        var next: ListNode? = head?.next

        while (cur != null) {
            if (cur.`val` == `val`) {
                println(prev?.`val`)
                println(cur?.`val`)
                println(next?.`val`)
                println()
                if (prev == null) {
                    cur = next
                    newHead = cur
                    next = cur?.next
                } else {
                    prev?.next = next
                    cur = next
                    next = cur?.next
                }

            } else {
                prev = cur 
                cur = next
                next = cur?.next
            }
        }

        return newHead
    }
}