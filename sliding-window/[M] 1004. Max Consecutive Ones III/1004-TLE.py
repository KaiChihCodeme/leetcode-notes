class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        if k == 0:
            cnt = 0
            for i in nums:
                if i == 1:
                    cnt += 1
                else:
                    ans = max(cnt, ans)
                    cnt = 0
            ans = max(cnt, ans)
            return ans

        for i in range(len(nums)):
            cnt_k = k
            ind = i
            cnt = 0
            while ind < len(nums) and (cnt_k != 0 or nums[ind] == 1):
                if nums[ind] == 0:
                    cnt_k -= 1
                cnt += 1
                ind += 1

            ans = max(ans, cnt)
        return ans

# time complexity: O(n^2)
# space complexity: O(1)
# this is a brute force solution with terrible time complexity
