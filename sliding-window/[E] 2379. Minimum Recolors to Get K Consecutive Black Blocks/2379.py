class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k-1

        # calculate the white in the init window
        ans = 0
        for i in range(r-l+1):
            if blocks[i] == 'W':
                ans += 1
        if ans == 0:
            return ans
        
        cur = ans
        # slide window to the end
        while r < len(blocks)-1:
            # if previous is white, minus the current val
            if blocks[l] == 'W':
                cur -= 1
            # slide to next position
            l += 1
            r += 1

            # if next is white, add current val
            if blocks[r] == 'W':
                cur += 1

            # if current is zero, means here is consecutive black blocks, directly return zero
            if cur == 0:
                return cur

            # find the min consecutive
            ans = min(cur, ans)

        return ans

# time complexity: O(n), where n is the length of blocks string
# space complexity: O(1), only use constant extra space