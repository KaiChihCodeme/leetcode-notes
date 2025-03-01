# 983
I can't solve it without hint.
But this is not that complicated.

we can refer to this solution: https://leetcode.com/problems/minimum-cost-for-tickets/solutions/810806/python-dp-solution-explanation
Concept: https://leetcode.com/problems/minimum-cost-for-tickets/solutions/226659/two-dp-solutions-with-pictures

- 1 day-pass can be calculate at any day -> `dp[i] = dp[i-1] + costs[0]` (every day plus 1-pass from previous day)
- 7 day-pass -> `dp[i] = dp[max(0, i-7)] + costs[1]` (every 7 days to pay the costs. So in the days of 7, we do not need to add costs until 7 days. Because before 7 days, we only need to get dp[0]+costs.)
- 30 day-pass -> `dp[i] = dp[max(0, i - 30)] + costs[2]` (concept is same as 7 day-pass)
- if current day is not in plan day, just pass the cost from previous -> `dp[i] = dp[i-1]`