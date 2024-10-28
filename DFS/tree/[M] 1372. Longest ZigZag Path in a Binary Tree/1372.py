# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # record the previous position (first: None, left: True, right: False)
        # if previous is False then current is True, it means it has zigzag
        # record the current node
        # record the current count
        stack = [(None, root, 1)]
        ans = 0

        while stack:
            previous_pos, cur, cnt = stack.pop()
            if cur.left:
                t_cnt = cnt
                # because if previous is right, it would be False, which can not differentiate from None (first)
                # the first must be 1, so we justify None at first, then check if it is False
                if previous_pos is None:
                    t_cnt = 1
                elif not previous_pos:
                    t_cnt += 1
                else:
                    t_cnt = 1
                
                # recourd the max count as ans
                if t_cnt > ans:
                    ans = t_cnt
                # store the next node and information
                stack.append((True, cur.left, t_cnt))
            if cur.right:
                t_cnt = cnt
                if previous_pos:
                    t_cnt += 1
                else:
                    t_cnt = 1

                if t_cnt > ans:
                    ans = t_cnt
                stack.append((False, cur.right, t_cnt))

        return ans

# time complexity: O(n)
# space complexity: O(n)