class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        ans = 0
        cnt_zero = 0

        # always keep zero count <= k, if > k, move left pointer
        # when we move left, we should decrease zero count if nums[l] == 0
        # if zero count <= k, update ans
        for r in range(len(nums)):
            # if we see a zero, increase zero count
            if nums[r] == 0:
                cnt_zero += 1

            # if zero count > k, move left pointer and see if left is zero, then decrease zero count
            if cnt_zero > k:
                if nums[l] == 0:
                    cnt_zero -= 1
                l += 1

            # if zero count <= k, it's feasible, update ans
            if cnt_zero <= k:
                ans = max(ans, r-l+1)
        
        return ans


# time complexity: O(n)
# space complexity: O(1)