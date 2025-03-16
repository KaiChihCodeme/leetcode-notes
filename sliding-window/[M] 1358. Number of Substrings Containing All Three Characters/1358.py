class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r, ans = 0, 0, 0
        sub_s = {'a', 'b', 'c'}
        sub_map = defaultdict(int)

        while l < len(s) or r < len(s):
            if len(sub_map) >= 3:
                ans += len(s) - r + 1

                if s[l] in sub_s:
                    sub_map[s[l]] -= 1
                    if sub_map[s[l]] == 0:
                        del sub_map[s[l]]
                
                l += 1
            else:
                if r == len(s):
                    break
                if s[r] in sub_s:
                    sub_map[s[r]] += 1
                r += 1
                
        return ans
        
# time complexity: O(n), where n is the length of s
# space complexity: O(1), since we only use a fixed-size dictionary to store three characters
# similar to 3306