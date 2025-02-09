class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        inc_dp = [] # increase dp from left to right
        des_dp = [] # descent dp from right to left

        # setup the dp array
        for _ in range(len(nums)):
            inc_dp.append(1)
            des_dp.append(1)

        # calculate the increase dp and descent dp
        for i in range(1, len(nums)):
            tmp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    # get the max one when calculate the comparison
                    tmp = max(tmp, inc_dp[j]+1)
            inc_dp[i] = tmp

        # iterate from right to left, to compare the numbers
        for m in range(len(nums)-2, -1, -1):
            tmp = 1
            for n in range(len(nums)-1, m, -1):
                if nums[m] > nums[n]:
                    tmp = max(tmp, des_dp[n]+1)
            des_dp[m] = tmp

        # calculate sum from inc_dp with des_dp
        max_sum = 0
        for k in range(len(nums)):
            # important in discard the 1 cases because it is not a mountain, it is a line
            if inc_dp[k] == 1 or des_dp[k] == 1:
                continue
            max_sum = max(max_sum, inc_dp[k]+des_dp[k])

        # add 1 due to we calculate the index twice
        return len(nums)-max_sum+1
    
# Time complexity: O(n^2)
# Space complexity: O(n)