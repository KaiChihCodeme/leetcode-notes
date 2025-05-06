# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        def recur(node):
            if not node: # no child, return 0
                return 0

            # get gain from left and right child
            # if the gain is negative, we ignore it
            # we only take positive gain
            gain_left = max(recur(node.left), 0)
            gain_right = max(recur(node.right), 0)

            # update the maximum path sum
            cur_sum = node.val + gain_left + gain_right
            self.ans = max(cur_sum, self.ans)

            # this value is for the prvious layer using. So for it, it only 
            # need one side of the child
            return node.val + max(gain_left, gain_right)

        recur(root)
        return self.ans
