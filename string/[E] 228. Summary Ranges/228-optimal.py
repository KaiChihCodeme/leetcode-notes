class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = [] # [start, end] or [x, y]
        for n in nums:
            if ranges and ranges[-1][1] == n-1:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])

        return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]

# time complexity: O(n)
# space complexity: O(n)

# e.g., input is [0,2,3,4,6,8,9]
# it will turn out to be [[0, 0], [2, 4], [6, 6], [8, 8]], which ranges[-1][1] is last element, [-1][0] is start index