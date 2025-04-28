# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        q = deque([(root, 1)])
        max_depth = 0

        while q:
            cur, depth = q.popleft()
            max_depth = max(max_depth, depth)
            
            if cur.left:
                q.append((cur.left, depth+1))
            
            if cur.right:
                q.append((cur.right, depth+1))

        return max_depth

# time complexity: O(n)
# space complexity: O(n)