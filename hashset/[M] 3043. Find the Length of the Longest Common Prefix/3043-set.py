class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_prefix = set()
        for i in arr1:
            si = str(i)
            tmp = ""
            for w in si:
                tmp += w
                arr1_prefix.add(tmp)
            
        leng = 0
        for j in arr2:
            sj = str(j)
            tmp = ""
            for jw in sj:
                tmp += jw
                if tmp in arr1_prefix:
                    leng = max(leng, len(tmp))

        return leng