class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_l = s.split(' ')
        if len(pattern) != len(s_l): return False

        m = {}
        m2 = {}

        for i in range(len(s_l)):
            if s_l[i] in m and m[s_l[i]] != pattern[i]:
                return False
            
            if pattern[i] in m2 and m2[pattern[i]] != s_l[i]:
                return False

            m[s_l[i]] = pattern[i]
            m2[pattern[i]] = s_l[i]

        return True
            
# time complexity o(n)
# space complexity o(n) 