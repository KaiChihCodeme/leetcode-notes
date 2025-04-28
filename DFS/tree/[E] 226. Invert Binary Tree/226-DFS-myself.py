# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]

        while stack:
            cur = stack.pop()

            cur.left, cur.right = cur.right, cur.left

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return root

# time complexity: O(n)
# space complexity: O(n)