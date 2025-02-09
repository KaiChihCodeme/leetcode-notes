class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        dic = {}

        # cal the total counts for nums
        prev = word[0]
        for ind, i in enumerate(word):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

            if i != prev:
                # update the comp
                l = dic[prev] // 9
                mod = dic[prev] % 9

                for j in range(l):
                    comp += ("9"+prev)
                if mod != 0:
                    comp += (str(mod)+prev)
                dic[prev] = 0

            if ind == len(word)-1:
                if not comp or comp[-1] != i:
                    # update the comp
                    l = dic[i] // 9
                    mod = dic[i] % 9

                    for j in range(l):
                        comp += ("9"+i)
                    if mod != 0:
                        comp += (str(mod)+i)

            prev = i
        
        return comp
    
# time complexity: O(n)
# space complexity: O(n)