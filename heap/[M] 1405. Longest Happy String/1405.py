class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""

        cur_a = 0
        cur_b = 0
        cur_c = 0
        total = a + b + c

        while total > 0:
            if (((a >= b and a >= c) and cur_a != 2) or (a > 0 and (cur_b == 2 or cur_c == 2))):
                ans += 'a'
                a -= 1
                cur_a += 1
                cur_b = cur_c = 0
            elif (((b >= a and b >= c) and cur_b < 2) or (b > 0 and (cur_a == 2 or cur_c == 2))):
                ans += 'b'
                b -= 1
                cur_b += 1
                cur_a = cur_c = 0
            elif (((c >= b and c >= a) and cur_c < 2) or (c > 0 and (cur_a == 2 or cur_b == 2))):
                ans += 'c'
                c -= 1
                cur_c += 1
                cur_a = cur_b = 0

            total -= 1

        return ans

# Time: O(n)
# Space: O(1)
            



