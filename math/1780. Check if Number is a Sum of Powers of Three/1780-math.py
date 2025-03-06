class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False

            n = n // 3

        return True

# time complexity: O(log n)
# space complexity: O(1)
# this solution is like 2^n bit calculation