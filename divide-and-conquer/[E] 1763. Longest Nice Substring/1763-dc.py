class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # stop condition
        if not s:
            return ""

        # set of s, to check if all elements' swapcase are in s
        ss = set(s)

        for ind, i in enumerate(s):
            # if i's swapcase not in s, we just drop this element and divide the problem into two subproblems
            if i.swapcase() not in ss:
                s1 = self.longestNiceSubstring(s[:ind])
                s2 = self.longestNiceSubstring(s[ind+1:])
                
                # due to we need to find the longest and earliest, so use >=
                if len(s1) >= len(s2):
                    return s1
                else:
                    return s2
                
        # if all of s is nice sting, return entire s
        return s