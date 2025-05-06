# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(cur, lis):
            if cur.left:
                inorder(cur.left, lis)
            
            lis.append(cur.val)

            if cur.right:
                inorder(cur.right, lis)

            return lis

        l = []
        res = inorder(root, l)
        
        return res[k-1]

        
# TC: O(N)
# SC: O(N)