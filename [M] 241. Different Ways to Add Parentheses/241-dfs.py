class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        m = {}
        return self.dfs(expression, m)

    def dfs(self, input, m):
        if input in m:
            return m[input]

        # the stop condition -> when input is only a digit
        if input.isdigit():
            m[input] = int(input)
            return [int(input)]

        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                # eval is a tricky function which can evaluate the string as a Python expression
                ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        m[input] = ret
        return ret

        
# Time Complexity: O(2^n), Space Complexity: O(2^n)


