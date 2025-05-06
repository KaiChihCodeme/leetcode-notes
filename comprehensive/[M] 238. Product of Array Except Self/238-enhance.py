class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dot = 1
        # sum of product
        for i in nums:
            dot *= i

        ans = []
        for ind, j in enumerate(nums):
            # if nums is zero, we need to calculate the product of all other numbers
            if j == 0:
                tmp = 1
                for k in range(len(nums)):
                    if k != ind:
                        tmp *= nums[k]
                ans.append(int(tmp))
            else:
                ans.append(int(dot/j))
        
        return ans

# time complexity: O(n^2)
# space complexity: O(n)