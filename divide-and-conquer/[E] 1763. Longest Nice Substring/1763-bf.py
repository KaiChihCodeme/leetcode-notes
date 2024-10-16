class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        # iterate each element
        for i in range(len(s)):
            # like a two pointer, if during this range has all swapcase, it means this is a nice substring
            for j in range(i+1, len(s)+1):
                if all(s[k].swapcase() in s[i:j] for k in range(i, j)):
                    # if new found length > original ans
                    if len(s[i:j]) > len(ans):
                        ans = s[i:j]

        return ans
