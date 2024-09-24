class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        leng = 0
        for i in arr1:
            for j in arr2:
                ind = 0
                tmp_len = 0
                i = str(i)
                j = str(j)
                word_len = min(len(i), len(j))
                while ind < word_len:
                    if i[ind] == j[ind]:
                        tmp_len += 1
                        ind += 1
                    else:
                        break

                leng = max(leng, tmp_len)

        return leng

    # TC: O(N^2) SC: O(N)