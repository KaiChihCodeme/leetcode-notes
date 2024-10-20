# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # res is the answer level, and index is the current level
        res = 1
        ind = 1
        q = deque([[root]])
        # store the temporary maximum sum
        maxi = root.val

        while q:
            cur_lvl = q.popleft()
            lvl = []

            # prepared the next level at first from current level's children
            for cur in cur_lvl:
                if cur.left:
                    lvl.append(cur.left)
                if cur.right:
                    lvl.append(cur.right)

            # calculate the sum of the next level
            if lvl:
                # because we would calculate the next level, so we need to increase the index
                ind += 1
                # calculate the sum of the next level and compare it with the maximum sum
                s = 0
                for l in lvl:
                    s += l.val
                if s > maxi:
                    maxi = s
                    res = ind

                # append the next level to the queue
                q.append(lvl)
        
        return res
            
# Time complexity: O(n)
# Space complexity: O(n)