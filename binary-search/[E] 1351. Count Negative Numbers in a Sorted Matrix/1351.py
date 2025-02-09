class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in grid:
            ind = 0
            flag = False
            target = 0
            l, r = 0, len(i)-1
            while l < r:
                m = l + (r-l) // 2
                if i[m] == 0:
                    ind = m+1
                    flag = True
                    break
                
                if i[m] > target:
                    l = m + 1
                else:
                    r = m

            if not flag:
                if i[l] < target:
                    ind = l
                else:
                    ind = l + 1
            
            while ind < len(i) and i[ind] == 0:
                ind += 1

            ans += len(i[ind:])
        return ans

# time complexity: O(nlogm), n is the number of rows, m is the number of columns
# space complexity: O(1)
