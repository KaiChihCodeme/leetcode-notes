# 198
We can find that this question is a DP question, we can use DP to decrease the time complexity.

And in my mind, I think we can iterate previous result on dp, but it will take O(N) times when we find maximum of previous DP values.

So, we can always store the maximum value on DP, and compare with `max(dp[cur-1], nums[cur]+dp[cur-2])` to get the maximum val in current index.