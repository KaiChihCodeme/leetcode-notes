class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        s = 0

        while s - n < 0:
            s += i
            i += 1

        return i - 2 if s != n else i-1

# Time complexity: O(n)
# Space complexity: O(1)