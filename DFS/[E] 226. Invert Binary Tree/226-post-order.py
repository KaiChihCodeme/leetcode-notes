# from https://leetcode.com/problems/invert-binary-tree/solutions/3199238/0-ms-simplest-solution-full-explanation-c-python3
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #Base Case
            return root
        self.invertTree(root.left) #Call the left substree
        self.invertTree(root.right)  #Call the right substree
        # Swap the nodes
        root.left, root.right = root.right, root.left
        return root # Return the root
    
# time complexity: O(n)
# space complexity: O(n)