class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= 0:
                r = m
            else:
                l = m + 1

        neg_len = l
        
        # if right contain 0
        while r < len(nums) and nums[r] == 0:
            r += 1

        pos_len = len(nums)-r

        # if all negative
        if l == r == len(nums)-1:
            return l+1
        
        return max(neg_len, pos_len)

# time complexity: O(log n), where n is the length of nums
# # space complexity: O(1), since we only use a constant amount of extra space