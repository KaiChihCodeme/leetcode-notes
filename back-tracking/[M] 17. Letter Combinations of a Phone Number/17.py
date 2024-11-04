class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = [] 
        m = {"2": {"a","b","c"}, "3": {"d", "e", "f"}, "4": {"g", "h", "i"}, "5": {"j", "k", "l"}, "6": {"m", "n", "o"}, 
        "7": {"p", "q", "r", "s"}, "8": {"t", "u", "v"}, "9": {"w", "x", "y", "z"}}

        tmp_lvl = 0
        total_lvl = len(digits)-1

        # lvl: the current level of all digits
        # digits: the given digits
        # tmp_str: the current string
        def recur(lvl, digits, tmp_str):
            # if level is greater than the total level, return
            if lvl > total_lvl:
                return

            # get the values of the current level
            vals = m[digits[lvl]]
            
            # if the current level is the last level, add the values to the answer
            # and stop the recursion
            if lvl == total_lvl:
                for i in vals:
                    ans.append(tmp_str+i)
            else:
                # if the current level is not the last level, continue the recursion
                # lvl + 1 and add the current element to the string        
                for j in vals:
                    recur(lvl+1, digits, tmp_str+j)                    

        # start the recursion (back-tracking)
        tmp_str = ""
        recur(tmp_lvl, digits, tmp_str)

        return ans
    
# time complexity: O(4^n)
# space complexity: O(4^n)