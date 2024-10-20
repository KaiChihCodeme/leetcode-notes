# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.arr1 = []
        self.arr2 = []

        def traverse(root, is_1):
            if not root:
                return None

            l = traverse(root.left, is_1)

            r = traverse(root.right, is_1)

            if not l and not r:
                if is_1:
                    self.arr1.append(root.val)
                else:
                    self.arr2.append(root.val)

            return True

        traverse(root1, True)
        traverse(root2, False)

        return self.arr1 == self.arr2

# TS: O(N)
# SC: O(N)