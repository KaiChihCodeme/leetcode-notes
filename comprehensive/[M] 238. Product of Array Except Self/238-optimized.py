class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dot = 1
        zero_cnt = 0

        # sum of product
        # if nums is zero, we need to calculate the product of all other numbers
        for i in nums:
            if i == 0:
                zero_cnt += 1
            else:
                dot *= i

        # if there are more than 1 zero, it will be 0
        if zero_cnt > 1:
            return [0] * len(nums)

        for ind, j in enumerate(nums):
            # if here exit one zero, only when value is 0, then it will have the dot
            if zero_cnt:
                if j != 0:
                    nums[ind] = 0
                else:
                    nums[ind] = dot
            else:
                nums[ind] = dot // j
        return nums

# time complexity: O(n)
# space complexity: O(1)
