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
    fun hasCycle(head: ListNode?): Boolean {
        /*
            iterate through the linked list 
            everytime i see a node, add that to my set
            while looking through the linked list, I always check if the currrent node is in the set already
                if it return true
                else add to set

            if im able to loop through the entire linked list, than return false
         */
         var ptr = head
         if (ptr == null) { return false }
         val set = mutableSetOf<ListNode>()

        while (ptr != null) {
            if (ptr !in set) {
                set.add(ptr)
            } else if (ptr in set) {
                return true
            }
            ptr = ptr?.next
        }
        return false
    }
}