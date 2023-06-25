# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
time: O(n) because algo loops over entire length of linked list when reversing
space: O(1) because algo the size of used vars such as 
       temp and nxt are a fixed size - doesn't scale to size of input
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = None
        nxt = head
        
        while (nxt != None):
            nxt = head.next 
            head.next = temp 
            temp = head 
            head = nxt 
            
        return temp
            
        