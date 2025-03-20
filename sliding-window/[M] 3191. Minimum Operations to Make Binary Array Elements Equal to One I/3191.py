class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l, r = 0, 2
        cnt = 0
        while r < len(nums):
            if nums[l] == 1:
                l += 1
                r += 1
                continue
            else:
                for i in range(l, r+1):
                    if nums[i] == 0:
                        nums[i] = 1
                    else:
                        nums[i] = 0
                cnt += 1
                l += 1
                r += 1
        
        # check
        for j in nums:
            if j != 1:
                return -1

        return cnt
        
# time complexity: O(n)
# space complexity: O(1)