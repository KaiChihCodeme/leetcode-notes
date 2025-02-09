class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums

        prev = None
        tmp = []
        ans = []

        for i in range(len(nums)):
            if prev is None:
                prev = nums[i]
                tmp.append(nums[i])
            else:
                if nums[i] - prev != 1:
                    if len(tmp) == 1:
                        ans.append(str(tmp[0]))
                        tmp = []
                    else:
                        ans.append("{0}->{1}".format(tmp[0], tmp[-1]))
                        tmp = []
                tmp.append(nums[i])
                prev = nums[i]

        if len(tmp) == 1:
            ans.append(str(tmp[0]))
        else:
            ans.append("{0}->{1}".format(tmp[0], tmp[-1]))

        return ans

# time complexity: O(n)
# space complexity: O(n)