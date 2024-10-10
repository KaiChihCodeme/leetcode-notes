class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)

# Time complexity: O(n)
# Space complexity: O(n)