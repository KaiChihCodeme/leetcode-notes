# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # bottom-up DFS, go through until leaf node, and return depth, also compare the depth with min_depth
        # in the end, return the min_depth as the result
        def getDepth(root, depth, min_depth):
            if root.left:
                min_depth = min(getDepth(root.left, depth+1, min_depth), min_depth)

            if root.right:
                min_depth = min(getDepth(root.right, depth+1, min_depth), min_depth)

            if not root.left and not root.right:
                return depth

            return min_depth

        return getDepth(root, 1, float('inf'))

            
