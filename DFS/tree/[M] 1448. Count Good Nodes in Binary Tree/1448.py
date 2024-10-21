# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        # store the current node and the maximum value from root to current node
        stack = [(root, root.val)]
        while stack:
            cur, maxi = stack.pop()
            if cur.val >= maxi:
                maxi = cur.val
                res += 1

            if cur.left:
                stack.append((cur.left, maxi))
            if cur.right:
                stack.append((cur.right, maxi))

        return res

# TC: O(N)
# SC: O(N)
