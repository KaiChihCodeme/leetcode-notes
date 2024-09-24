class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # spepcial case
        if n == 1:
            return True

        if n == 0:
            return False

        # divide by 2 and at the end will be 1 of mod 0
        if n % 2 != 0:
            return False

        if n // 2 == 1:
            return True
        else:
            return self.isPowerOfTwo(n//2)