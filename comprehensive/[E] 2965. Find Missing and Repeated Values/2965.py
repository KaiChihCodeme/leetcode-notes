class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid)
        res = []

        s = set()
        for i in range(len(grid)):
            for j in grid[i]:
                if j in s:
                    res.append(j)
                else:
                    s.add(j)

        for check in range(1, n+1):
            if check not in s:
                res.append(check)

        return res

# time complexity: O(N^2)
# space complexity: O(N)