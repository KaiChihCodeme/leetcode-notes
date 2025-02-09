# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root, tmp):
            tmp += str(root.val)

            if root.left:
                dfs(root.left, tmp)
            
            if root.right:
                dfs(root.right, tmp)

            if not root.left and not root.right:
                self.ans += int(tmp)

        dfs(root, "")

        return self.ans

# time complexity: O(n)
# space complexity: O(n)

