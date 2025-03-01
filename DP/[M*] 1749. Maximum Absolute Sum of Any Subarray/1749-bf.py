class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            tmp_sum = 0
            for j in range(i, len(nums)):
                tmp_sum += nums[j]
                res = max(res, abs(tmp_sum))

        return res

# time complexity: O(n^2)
# space complexity: O(1)