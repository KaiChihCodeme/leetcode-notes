class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        while l < r:
            mid = l + (r - l) // 2
            cnt = 0
            skip = False

            for i in nums:
                if skip:
                    skip = False
                    continue

                if i <= mid:
                    cnt += 1
                    skip = True
            
            if cnt >= k:
                r = mid
            else:
                l = mid + 1

        return l

# time complexity: O(n * log(max(nums))), where n is the length of nums
# space complexity: O(1), since we only use a few variables regardless of input size