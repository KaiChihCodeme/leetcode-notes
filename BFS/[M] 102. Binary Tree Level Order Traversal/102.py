# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root:
            return ans

        cur_q = deque([root])
        

        while True:
            cur_l = []
            next_q = deque([])

            while cur_q:
                cur = cur_q.popleft()
                cur_l.append(cur.val)
                if cur.left:
                    next_q.append(cur.left)
                if cur.right:
                    next_q.append(cur.right)
                
            ans.append(cur_l)
            cur_q = next_q

            if not cur_q:
                return ans

# time complexity: O(n)
# space complexity: O(n)
            



