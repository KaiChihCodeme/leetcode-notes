# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        ans = ListNode()
        res = ans

        while cur1 or cur2:
            if cur1 is None and cur2:
                res.next = ListNode(cur2.val)
                res = res.next
                cur2 = cur2.next
            elif (cur1 and cur2 is None) or cur1.val <= cur2.val:
                res.next = ListNode(cur1.val)
                res = res.next
                cur1 = cur1.next
            else:
                res.next = ListNode(cur2.val)
                res = res.next
                cur2 = cur2.next

        return ans.next