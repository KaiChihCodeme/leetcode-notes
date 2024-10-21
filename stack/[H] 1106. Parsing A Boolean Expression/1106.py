class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for i in expression:
            if i == ")":
                # pop until find "("
                s = set()
                while True:
                    cur = stack.pop()
                    if cur == ",":
                        continue
                    if cur != "(":
                        s.add(cur)
                    else:
                        break
                ope = stack.pop()

                # operate
                new = None
                if len(s) > 1:
                    if ope == "|":
                        new = True
                    elif ope == "&":
                        new = False
                else:
                    o = None
                    for j in s:
                        if j == "t":
                            o = True
                        else:
                            o = False
                    if ope == "!":
                        new = not o
                    else:
                        new = o

                new_o = "f"
                if new:
                    new_o = "t" 
                stack.append(new_o)

            # do not need to consider ")"
            if i != ")":
                stack.append(i)

        return True if stack[0] == 't' else False
    
# Time complexity: O(n)
# Space complexity: O(n)