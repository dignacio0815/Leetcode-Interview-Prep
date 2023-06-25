# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = None
        cur = head
        nxt = head
        
        while (nxt != None):
            nxt = cur.next 
            cur.next = temp 
            temp = cur 
            cur = nxt 
            
        return temp
            
        