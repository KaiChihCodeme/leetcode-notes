# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, root.val)]
        ans = 0
        while stack:
            cur, cur_maxi = stack.pop()

            # process the max one
            if cur.val >= cur_maxi:
                ans += 1
                cur_maxi = cur.val
            
            if cur.left:
                stack.append((cur.left, cur_maxi))
            if cur.right:
                stack.append((cur.right, cur_maxi))
            

        return ans

            
# TC: O(N)
# SC: O(N)