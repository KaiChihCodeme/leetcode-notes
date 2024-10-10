class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        r = n - 1
        while l < r:
            m = l + (r - l) // 2
            cnt = 0
            for i in nums:
                if i <= m:
                    cnt += 1
            
            if cnt <= m:
                l = m + 1
            else:
                r = m
                
        return l