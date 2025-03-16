class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l, r = 0 , k-1
        ans = 0
        found = False

        while l < len(colors):
            if found:
                # last found, just check the right index
                if colors[r%len(colors)] != colors[r%len(colors)-1]:
                    # still match, do not need to check entire again
                    found = True
                else:
                    # do not match, means before right index, there always duplicated
                    found = False
                    # update left and right index here
                    l = r
                    r = l + k - 1
                    # no need to run under process
                    continue
            else:
                # iterate entire range to check
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
    
# time complexity: O(n*k), where n is the length of colors array and k is the given length of each group
# space complexity: O(1), only using constant extra space for variables
# this solution better than TLE solution due to we can avoid checking repeat elements