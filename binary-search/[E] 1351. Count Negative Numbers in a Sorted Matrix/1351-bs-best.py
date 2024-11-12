class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in grid:
            # the difference is right index must be len(i) instead of len(i)-1
            l, r = 0, len(i)
            while l < r:
                m = l + (r-l) // 2
                
                # should >= 0 to move left index, because we only need to find out the first negative num
                if i[m] >= 0:
                    l = m + 1
                else:
                    r = m
        
            ans += len(i)-l
        return ans

# time complexity: O(nlogm), n is the number of rows, m is the number of columns
# space complexity: O(1)
