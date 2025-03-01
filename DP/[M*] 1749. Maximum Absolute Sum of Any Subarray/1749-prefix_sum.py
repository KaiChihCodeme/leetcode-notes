class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s, mi, ma= 0, 0, 0
        for i in nums:
            s += i
            mi = min(mi, s)
            ma = max(ma, s)
        return ma-mi

# time complexity: O(n)
# space complexity: O(1)