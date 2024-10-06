class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for ind, i in enumerate(nums):
            right_sum -= i
            if right_sum == left_sum:
                return ind
            left_sum += i
        return -1