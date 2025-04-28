class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def cal_cnt(query):
            q = deque()
            seen = set()
            q.append((0,0))
            cnt = 0

            while q:
                x, y = q.popleft()
                if (x,y) in seen:
                    continue
                else:
                    seen.add((x,y))

                if grid[x][y] > query:
                    return cnt
                cnt += 1
                
                if x + 1 < len(grid) and grid[x+1][y] < query:
                    q.append((x+1, y))
                if x - 1 >= 0 and grid[x-1][y] < query:
                    q.append((x-1, y))
                if y + 1 < len(grid[0]) and grid[x][y+1] < query:
                    q.append((x, y+1))
                if y - 1 >= 0 and grid[x][y-1] < query:
                    q.append((x, y-1))
            return cnt

        ans = []
        for i in queries:
            ans.append(cal_cnt(i))
        return ans

# time complexity: O(Q * M * N) where Q is the length of queries and M, N are the dimensions of the grid
# space complexity: O(M * N) where M and N are the dimensions of the grid (for storing seen set)
            