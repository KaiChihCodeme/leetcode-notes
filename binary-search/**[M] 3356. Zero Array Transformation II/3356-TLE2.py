class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        cnt = 0

        s = set(nums)
        if len(s) == 1 and s.pop() == 0:
            return cnt

        for i in queries:
            tmp_arr = []
            tmp_ind = 0
            while tmp_ind < len(nums):
                if tmp_ind >= i[0] and tmp_ind <= i[1]:
                    tmp_arr.append(i[2])
                else:
                    tmp_arr.append(0)
                tmp_ind += 1

            for j in range(len(nums)):
                nums[j] -= tmp_arr[j]
                if nums[j] < 0:
                    nums[j] = 0

            cnt += 1

            s = set(nums)
            if len(s) == 1 and s.pop() == 0:
                return cnt

            

        return -1