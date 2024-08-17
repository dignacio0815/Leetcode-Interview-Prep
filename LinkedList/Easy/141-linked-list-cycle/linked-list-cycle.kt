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
        return twoPointerApproach(head)
    }

    fun twoPointerApproach(head: ListNode?): Boolean {
        /*
        keep 2 pointers pointed to head and head.next.next
        the reason we do 2 nexts is because, if it was only going to be 1 next, than this would have solved example 2

        for example,
            slow pointer is head
            fast pointer is head.next.next
            in example 2, this would continuously loop since they never intersect
            but with head.next.next eventually the 2 would intersect confirming a cycle

        proof:
            slow pointer at head
            fast pointer at head.next.next
            keep looping each to the next and eventually they should intersect
            if they do, its a cycle
            else reaches end of linked list, not a cycle
         */
         if (head == null) {return false}
         var slow = head
         var fast = head?.next?.next

         while (slow != null) {
            if (slow == fast) {
                return true
            }
            slow = slow?.next
            fast = fast?.next?.next
         }
         return false
    }

    fun setApproach(head: ListNode?): Boolean {
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