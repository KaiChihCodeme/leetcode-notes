class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1

        last = 1
        ans = 0
        for _ in range(n-1):
            ans += (2 * last)
            last += 2

        return ans+last

# time complexity: O(n)
# space complexity: O(1)