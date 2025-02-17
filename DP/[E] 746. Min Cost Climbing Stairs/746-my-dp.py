class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)

        for ind in range(len(cost)-1, -1, -1):
            if ind == len(cost)-1:
                dp[ind] = cost[-1]
                continue
            
            dp[ind] = min(cost[ind]+dp[ind+1], cost[ind]+dp[ind+2])

        return min(dp[0], dp[1])

# Time complexity: O(n)
# Space complexity: O(n)