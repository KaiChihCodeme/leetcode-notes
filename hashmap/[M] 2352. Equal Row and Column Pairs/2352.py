class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = {}
        for i in grid:
            st = str(i)
            if st not in m:
                m[st] = 1
            else:
                m[st] += 1


        ans = 0
        for i in range(len(grid[0])):
            tmp = []
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            
            if str(tmp) in m:
                ans += m[str(tmp)]

        return ans

# time complexity: O(n^2)
# space complexity: O(n^2)
# it's brute force, which need to be enhanced