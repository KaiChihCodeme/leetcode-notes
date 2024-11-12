"""
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.
"""
from collections import deque
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = []
        for i in range(len(grid)):
            dp.append([])
            for j in range(len(grid[0])):
                dp[i].append(0)

        # find initial point in the first column
        tmp = deque()
        for k in range(len(grid)):
            tmp.append((k, 0))

        while tmp:
            row, col = tmp.popleft()
            if col + 1 >= len(grid[0]):
                continue
            
            possible = [(row, col+1)]
            if row-1 >= 0:
                possible.append((row-1, col+1))
            if row+1 < len(grid):
                possible.append((row+1, col+1))

            # compare
            for r, c in possible:
                if grid[r][c] > grid[row][col]:
                    dp[r][c] = dp[row][col]+1
                    tmp.append((r,c))

        return max(map(max, dp))

            
# time complexity: O(n*m)
# space complexity: O(n*m)
            
