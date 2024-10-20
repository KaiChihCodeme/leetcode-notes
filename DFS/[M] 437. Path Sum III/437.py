# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        if not root:
            return res

        stack = [(root, [])]

        while stack:
            # tmp will store the path from root to current node
            cur, tmp = stack.pop()
            
            # base on tmp, we will calculate the new tmp from this current node
            ntmp = []
            # iterate through the path from root to current node
            for i in tmp:
                ntmp.append(i + cur.val)
            
            # calculate the number of path that sum up to targetSum
            for j in ntmp:
                if targetSum == j:
                    res += 1
            
            # if the current node value is equal to targetSum, we will add 1 to res
            if cur.val == targetSum:
                res += 1
            # append current node to ntmp for next round
            ntmp.append(cur.val)

            if cur.left:
                stack.append((cur.left, ntmp))
            if cur.right:
                stack.append((cur.right, ntmp))

        return res

# TC: O(N^2)
# SC: O(N^2)
