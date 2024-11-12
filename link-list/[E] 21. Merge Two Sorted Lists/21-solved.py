# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode(0)
        cp = cur
        
        while l1 and l2:
            if l1.val <= l2.val:
                cp.next = l1
                cp = cp.next
                l1 = l1.next
            elif l2.val < l1.val:
                cp.next = l2
                cp = cp.next
                l2 = l2.next
        
        while l1:
            cp.next = l1
            cp = cp.next
            l1 = l1.next
        
        while l2:
            cp.next = l2
            cp = cp.next
            l2 = l2.next
            
        return cur.next