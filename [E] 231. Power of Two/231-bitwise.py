class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Special case
        if n <= 0:
            return False
        # Use bitwise operation to check if n is a power of two
        return (n & (n - 1)) == 0