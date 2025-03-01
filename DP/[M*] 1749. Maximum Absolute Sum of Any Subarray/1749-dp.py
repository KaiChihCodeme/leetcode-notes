class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_dp = [0] * (len(nums)+1)
        min_dp = [0] * (len(nums)+1)

        for i in range(1, len(nums)+1):
            # nums[i-1] means the current index of nums
            max_dp[i] = max(max_dp[i-1]+nums[i-1], nums[i-1])
            min_dp[i] = min(min_dp[i-1]+nums[i-1], nums[i-1])
        max_res = max(max_dp)
        min_res = min(min_dp)

        return max(max_res, abs(min_res))

# time complexity: O(n)
# space complexity: O(n)