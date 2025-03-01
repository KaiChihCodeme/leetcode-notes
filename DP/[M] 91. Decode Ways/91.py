class Solution:
    def numDecodings(self, s: str) -> int:
        c1 = 0 if s[0] == "0" else 1
        c2 = 0
        for ind in range(1, len(s)):
            tmp_c1 = c1
            if s[ind] == "0":
                c1 = 0
            else:
                c1 = c1 + c2
            c2 = tmp_c1 if int(s[ind-1:ind+1]) <= 26 else 0

        return c1+c2
            
# time complexity: O(n)
# space complexity: O(1)