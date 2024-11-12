from collections import deque
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dirs = [(-1,1),(0,1),(1,1)]

        n_r, n_c = len(grid), len(grid[0])
        # create a seen dp
        seen = [[False for i in range(n_c)] for j in range(n_r)]
        
        ans = 0
        q = deque()

        # create the first colunmn
        for k in range(n_r):
            q.append((k, 0, 0))

        while q:
            # using BFS for processing current len elements
            for _ in range(len(q)):
                row, col, cnt = q.popleft()

                # update maximum count when pop
                ans = max(ans, cnt)

                # iterate all possible path from current position
                for dr, dc in dirs:
                    new_row = row + dr
                    new_col = col + dc

                    # the additional part is, consider seen to avoid repetitive calculation
                    # due to we only go through right, the maximum of current will be within current colmn
                    # for example, if we conduct to (1,3) then the maximum only be 3 in any rows if follows rule
                    if 0 <= new_row < n_r and new_col < n_c and not seen[new_row][new_col] and grid[new_row][new_col] > grid[row][col]:
                        q.append((new_row, new_col, cnt+1))
                        seen[new_row][new_col] = True
        
        return ans
                

# Time: O(N*M)
# Space: O(N*M)

# The best solution to me due to it is similar to my first thought but suffer from Memory Limit Exceeded
# Here provide a solution to avoid repetitive calculation by using seen dp 
            
            
