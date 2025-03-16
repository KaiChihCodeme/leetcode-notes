class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        s = []
        sn = []
        for i in nums:
            if i > 0:
                s.append(i)
            elif i < 0:
                sn.append(i)

        return max(len(s), len(sn))

# time complexity: O(n), where n is the length of nums
# space complexity: O(n), where n is the length of nums