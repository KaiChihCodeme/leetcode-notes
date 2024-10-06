class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operator = ('+', '-', '*')
        memo = dict()
        # it would be: {"1-1": [0], "2-1-1": [0, 2], ...}
        
        def rule(inp, l, r):
            if inp == '+':
                return l + r
            elif inp == '-':
                return l - r
            elif inp == '*':
                return l * r
            
        def ways(s):
            if s in memo:
                return memo[s]
            ans = []

            for i in range(len(s)):
                if s[i] in operator:
                    oper = s[i]
                    l = ways(s[:i])
                    r = ways(s[i+1:])
                    
                    for i in l:
                        for j in r:
                            ans.append(rule(oper, int(i), int(j)))

            if len(ans) == 0:
                ans.append(int(s))
            memo[s] = ans

            return ans

        return ways(expression)

# TC: O(2^N), Space Complexity: O(2^N)
