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
        return optimal(head)
        // return bruteForce(head)
    }

    fun optimal(head:ListNode?):Boolean {
        /*
            get the length of the linked list
            loop until halfway point
            if length is even, move midPtr by 1 
            reverse remaining right part of linked list
            take head and head of reversed linked list and compare only returning false if there's a mismatch
         */

        var length = 0
        var ptr = head
        while (ptr != null) {
        length+=1
        ptr = ptr?.next
        }

        ptr = head
        
        for (i in 0 until length - length.floorDiv(2)) {
        ptr = ptr?.next
        }

        var prev:ListNode? = null
        var cur:ListNode? = ptr
        var next:ListNode? = cur?.next

        while (cur != null) {
        cur?.next = prev
        prev = cur
        cur = next
        next = cur?.next
        }

        var h = head
        while (prev != null) {
        prev 
        if (prev?.`val` != h?.`val`) {return false}
        h = h?.next
        prev = prev?.next
        }
        return true
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