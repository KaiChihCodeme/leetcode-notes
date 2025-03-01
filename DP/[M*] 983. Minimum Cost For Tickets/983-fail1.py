class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxi = max(days)
        dp = [0] * maxi

        s_days = set(days)

        for i in range(maxi):
            cur = dp[i-1] if i > 0 else 0

            if i+1 not in s_days:
                dp[i] = min(cur, dp[i]) if dp[i] != 0 else cur
            else:
                # 3 choice
                dp[i] = cur+costs[0] if dp[i]==0 else min(dp[i], cur+costs[0])
                if i + 6 < maxi:
                    dp[i+6] = cur+costs[1] if dp[i+6]==0 else min(dp[i+6], cur+costs[1])
                if i + 29 < maxi:
                    dp[i+29] = cur+costs[2] if dp[i+6]==0 else min(dp[i+29], cur+costs[2])

        return dp[-1]
