# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        ind = 1
        rev = ListNode()
        rev_flag = False

        if left == right:
            return head

        rem = None

        # reverse the scope of linked list
        while cur:
            if left == ind:
                rev.val = cur.val
                rev.next = None
                rev_flag = True
            elif rev_flag and ind <= right:
                l = ListNode(cur.val, rev)
                rev = l

            if ind > right:
                rem = cur
                break

            ind += 1
            cur = cur.next

        # process the new linked list
        cur = head
        if left == 1:
            cur.next = rev
            head = cur.next
            
        ind = 1

        while cur:
            if ind == left - 1:
                cur.next = rev

            if not cur.next:
                cur.next = rem
                break
            cur = cur.next
            ind += 1

        return head
        
# time complexity: O(n)
# space complexity: O(1)