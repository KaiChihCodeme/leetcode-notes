class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1):
            ans.append(ans[i//2] + i % 2)

        return ans

# time complexity: O(N)
# space complexity: O(N)