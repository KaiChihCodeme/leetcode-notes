class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxi = days[-1]+1
        dp = [0] * maxi

        s_days = set(days)

        for i in range(maxi):
            if i not in s_days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0], dp[max(0, i-7)]+costs[1], dp[max(0, i-30)]+costs[2])

        return dp[-1]

# time complexity: O(n)
# space complexity: O(n)