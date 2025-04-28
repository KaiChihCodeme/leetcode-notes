class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = []
        for i in range(len(grid)):
            for j in grid[i]:
                flat.append(j)

        flat.sort()

        # find the med one and calculate 
        med = flat[len(flat)//2]

        cnt = 0
        # count how many times can we get to med
        for k in flat:
            if abs(k-med) % x != 0:
                return -1
            cnt += abs(k - med) // x

        return cnt
    
# time complexity: O(N*M*log(N*M)) where N and M are the dimensions of the grid (for sorting)
# space complexity: O(N*M) where N and M are the dimensions of the grid (for storing flat array)