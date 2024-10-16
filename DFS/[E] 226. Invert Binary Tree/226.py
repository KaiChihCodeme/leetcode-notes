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

        new_t = TreeNode(root.val)
        stack = [(root, new_t)]
        while stack:
            r, t = stack.pop()
            if not r:
                continue
            if r.left and r.right:
                t.left = TreeNode(r.right.val)
                t.right = TreeNode(r.left.val)

                stack.append((r.left, t.right))
                stack.append((r.right, t.left))
            elif r.left:
                t.right = TreeNode(r.left.val)

                stack.append((r.left, t.right))
                stack.append((r.right, t.right))
            elif r.right:
                t.left = TreeNode(r.right.val)

                stack.append((r.left, t.left))
                stack.append((r.right, t.left))

        return new_t

# time complexity: O(n)
# space complexity: O(n)