class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # it's a very intuitive way, and I have used division :(
        ans = []
        for ind, i in enumerate(nums):
            if ind == 0:
                dot = 1
                for j in nums[1:]:
                    dot *= j
                ans.append(dot)
            elif i == 0:
                dot = 1
                fp = nums[:ind]
                bp = nums[ind+1:]
                for k in fp:
                    dot *= k
                for m in bp:
                    dot *= m
                ans.append(dot)
            else:
                ans.append((int)(ans[ind-1] / i * nums[ind-1]))

        return ans

# time complexity: O(n^2)
# space complexity: O(n)
# note: the time complexity is expected to be O(n) in question, so I need to optimize it.