# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ans = ListNode(head.val)
        cur = ans

        # process the first step
        if head.next is None:
            return ans

        # process odd
        odd_trace = head.next.next
        while odd_trace is not None:
            cur.next = ListNode(odd_trace.val)
            cur = cur.next

            if odd_trace.next is None or odd_trace.next.next is None:
                break
            odd_trace = odd_trace.next.next

        # process even
        even_trace = head.next
        while even_trace is not None:
            cur.next = ListNode(even_trace.val)
            cur = cur.next

            if even_trace.next is None or even_trace.next.next is None:
                break
            even_trace = even_trace.next.next

        return ans