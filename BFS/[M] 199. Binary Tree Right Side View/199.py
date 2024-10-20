# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque()
        q.append([root])

        while q:
            cur_lvl = q.popleft()
            # for the next level from current level
            lvl = []

            # construct the next level
            for cur in cur_lvl:
                if cur.left:
                    lvl.append(cur.left)
                if cur.right:
                    lvl.append(cur.right)
            # append the rightmost node value to res
            res.append(cur_lvl[-1].val)

            # if there is a next level, we will append it to q. Otherwise, we will stop the loop
            if lvl:
                q.append(lvl)

        return res
            
# TC: O(N)
# SC: O(N)