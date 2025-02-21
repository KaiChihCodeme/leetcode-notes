class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            prev = i - 2
            if prev < 0:
                dp[i] = nums[i]
                continue
            
            dp[i] = nums[i] + max(dp[:prev+1])

        return max(dp)

# time complexity: O(n^2)
# space complexity: O(n)