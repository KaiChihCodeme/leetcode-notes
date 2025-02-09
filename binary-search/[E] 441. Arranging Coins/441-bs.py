class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = l + (r - l) // 2
            coinUsed = m * (m + 1) // 2 # it is math, e.g., n = 4, coinUsed = 10, which is 1+2+3+4
            
            if coinUsed == n:
                return m
            
            if coinUsed < n:
                l = m + 1
            else:
                r = m - 1
                
        return r
    
# Time complexity: O(logn)
# Space complexity: O(1)