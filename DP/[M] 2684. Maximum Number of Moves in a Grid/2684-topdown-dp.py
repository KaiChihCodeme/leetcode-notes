class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        r_n, c_n, dirs = len(grid), len(grid[0]), [(-1, 1), (0, 1), (1, 1)]
        @cache
        def dp(rows, columns):
            # calculate the maximum every possible directions
            ans = 0
            for nr, nc in dirs:
                new_rows = rows+nr
                new_columns = columns+nc
                if new_rows >= 0 and new_rows < r_n and new_columns < c_n and grid[new_rows][new_columns] > grid[rows][columns]:
                    # calculate until reach bottom, return the sum depth
                    ans = max(ans, 1+dp(new_rows, new_columns))
            return ans

        # start from first column
        return max(dp(i, 0) for i in range(r_n))

# time complexity: O(n*m)
# space complexity: O(n*m)

# The most tricky is, we need to add @cache to avoid TLE, because the time complexity is O(n*m), which is not acceptable for the problem.
            
            
            
