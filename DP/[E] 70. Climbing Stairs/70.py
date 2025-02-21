class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n+1)

        for i in range(1, n+1):
            cnt = 0
            cnt += dp[i-1]
            cnt += dp[i-2] if i > 1 else 0

            dp[i] = cnt

        return dp[-1]

# time complexity: O(n)
# space complexity: O(n)