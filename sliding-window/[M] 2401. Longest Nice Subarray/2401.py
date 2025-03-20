class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, r = 0, 1
        ans = 1
        
        while r != len(nums):
            if self.check(nums, l, r):
                r += 1
            else:
                l += 1
                r += 1
            ans = max(ans, r-l)
        return ans
            

    def check(self, nums, l, r):
        for i in range(l, r):
            for j in range(i+1, r+1):
                if (nums[i] & nums[j]) != 0:
                    return False

        return True
                

# time complexity: O(n^3)
# space complexity: O(1)


        