class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l, r = 0 , k-1
        ans = 0

        while l < len(colors):
            found = True
            for i in range(l+1, l+(r-l)+1):
                if colors[i%len(colors)] == colors[(i-1)%len(colors)]:
                    found = False
                    break
            
            if found:
                ans += 1

            l += 1
            r += 1

        return ans

# time complexity: O(n * k), where n is the length of colors array and k is the given integer
# space complexity: O(1), as we only use a constant amount of extra space
# TLE Solution