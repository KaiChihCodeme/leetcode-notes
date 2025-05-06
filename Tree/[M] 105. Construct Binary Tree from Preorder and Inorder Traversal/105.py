# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            mid = inorder.index(preorder.pop(0))
            x = TreeNode(inorder[mid])
            
            x.left = self.buildTree(preorder, inorder[:mid])
            x.right = self.buildTree(preorder, inorder[mid+1:])
        return x
    
# # TC: O(N)
# # SC: O(N)