# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)

        if left_depth == right_depth:
            # means the left tree is a complete bt
            # after calculating left complete binary tree, then calculating the remain left one.
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            # means the right tree is a complete bt
            # after calculating left complete binary tree, then calculating the remain left one.
            return pow(2, right_depth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
    
# Time complexity: O(logn * logn), where logn is the depth of the tree. (get depth is logn, and count nodes [recursion] is logn)
# Space complexity: O(logn) for the recursion stack.