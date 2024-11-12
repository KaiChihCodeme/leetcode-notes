class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        tmp = ""
        for ind, i in enumerate(chars):
            # once we see a different character, we add the previous character to the string
            if tmp and tmp[-1] != i:
                cnt = len(tmp)
                s += tmp[0]
                # only add the count if it's greater than 1
                if cnt > 1:
                    s += str(cnt)
                # reset the tmp
                tmp = ""

            # add the character to the tmp
            tmp += i

            # if reach the end, add the last character to the string
            if ind == len(chars)-1:
                s += tmp[0]
                if len(tmp) > 1:
                    s += str(len(tmp))

        # update to the input list
        for a in range(len(s)):
            chars[a] = s[a]

        # trim the list and return length
        return len(chars[:len(s)])
        
# Time complexity: O(N)
# Space complexity: O(1)