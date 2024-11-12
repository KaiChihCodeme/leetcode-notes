class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums

        l = nums[0]
        r = nums[-1]

        tmp_l = []
        ind = 0
        res = []
        for i in range(l, r+1):
            if nums[ind] == i:
                tmp_l.append(i)
                ind += 1
            else:
                if tmp_l:
                    if len(tmp_l) == 1:
                        res.append(str(tmp_l[0]))
                    else:
                        res.append("{0}->{1}".format(tmp_l[0], tmp_l[-1]))
                    tmp_l = []

        if tmp_l:
            if len(tmp_l) == 1:
                res.append(str(tmp_l[0]))
            else:
                res.append("{0}->{1}".format(tmp_l[0], tmp_l[-1]))

        return res

# time complexity: O(n)
# space complexity: O(n)