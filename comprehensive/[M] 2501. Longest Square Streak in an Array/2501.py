class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)

        m = -1
        for j in nums:
            cnt = 1
            tmp = j
            # calculate the squares always start from the j
            while tmp ** 2 in s:
                cnt += 1
                if cnt > m:
                    m = cnt
                tmp = tmp ** 2

        return m

# Time Complexity: O(n)
# Space Complexity: O(n)