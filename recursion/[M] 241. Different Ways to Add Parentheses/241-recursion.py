class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operator = ('+', '-', '*')
        
        def rule(inp, l, r):
            if inp == '+':
                return l + r
            elif inp == '-':
                return l - r
            elif inp == '*':
                return l * r
            
        def ways(s):
            ans = []
            for i in range(len(s)):
                if s[i] in operator:
                    # Divide and Conquer, ex: 2*3-4*5, it would be 2*(3-4*5) -> 3-(4*5) -> 4 * 5, ..., then combine back
                    oper = s[i]
                    left = s[:i]
                    right = s[i+1:]

                    l = ways(left)
                    r = ways(right)

                    for i in l:
                        for j in r:
                            ans.append(rule(oper, int(i), int(j)))

            # stop condition, if there has no operator, then return the number
            if len(ans) == 0:
                ans.append(int(s))

            return ans

        return ways(expression)

# TC: O(2^N), Space Complexity: O(2^N)
