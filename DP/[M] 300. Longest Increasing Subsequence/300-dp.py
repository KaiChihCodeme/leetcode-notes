class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for ind in range(1,len(nums)):
            tmp = 1
            for k in range(ind):
                if nums[ind] > nums[k]:
                    tmp = max(tmp, dp[k]+1)
            dp[ind] = tmp
        return max(dp)
        
# Time complexity: O(n^2)
# Space complexity: O(n)

            