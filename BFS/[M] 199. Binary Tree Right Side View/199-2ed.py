# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root: return ans

        q = deque([root])

        while q:
            lvl = []
            for _ in range(len(q)):
                cur = q.popleft()
                lvl.append(cur.val)

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
            ans.append(lvl[-1])
        return ans

# TC: O(N)
# SC: O(N)