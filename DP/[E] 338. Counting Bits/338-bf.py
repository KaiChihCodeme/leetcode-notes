class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            s = format(i, 'b')
            sum_bin = sum([int(j) for j in s])
            ans.append(sum_bin)

        return ans

        
# time complexity: O(N^2)
# space complexity: O(N)