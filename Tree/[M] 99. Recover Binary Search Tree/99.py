# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # this would only have two nodes need to be recovered
        self.tmp_1 = None
        self.tmp_2 = None

        # use inorder traversal to find those two nodes
        # because in BST, inorder traversal would be sorted
        def inorder(root):
            if not root:
                return

            inorder(root.left)

            # if root < previous, it means this is a wrong node
            # the first wrong node would be the previous node
            if self.tmp_1 is None and root.val < self.previous.val:
                self.tmp_1 = self.previous
                self.tmp_2 = root
            # the second wrong node would be the current node
            if self.tmp_1 is not None and root.val < self.previous.val:
                self.tmp_2 = root

            # update previous node
            self.previous = root

            inorder(root.right)

        self.previous = TreeNode(float("-inf"))
        inorder(root)

        # swap those two nodes
        tmp = self.tmp_1.val
        self.tmp_1.val = self.tmp_2.val
        self.tmp_2.val = tmp

        return root

# Time Complexity: O(n)
# Space Complexity: O(n)
