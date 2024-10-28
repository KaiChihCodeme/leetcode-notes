# refer to this solution: https://leetcode.com/problems/min-cost-climbing-stairs/solutions/773865/a-beginner-s-guide-on-dp-validation-how-to-come-up-with-a-recursive-solution-python-3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(c):
            # base case due to we only have two steps
            if c < 2:
                return cost[c]

            # we only climb one step or two steps at a time, so we can only reach the current step from the previous step or the step before the previous step
            # then calculate the cost of reaching the current step in recursively
            return cost[c] + min(dp(c-1), dp(c-2))

        l = len(cost)
        # start from 0 or 1
        return min(dp(l-1), dp(l-2))
    
# Time complexity: O(n)
# Space complexity: O(n)
# this solution will reach time limit exceeded when the input is large