class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        cnt = 0

        s = set(nums)
        if len(s) == 1 and s.pop()==0:
            return cnt

        for i in queries:
            for j in range(i[0], i[1]+1):
                nums[j] -= i[2]
                if nums[j] < 0:
                    nums[j] = 0
            cnt += 1
            s = set(nums)
            if len(s) == 1 and s.pop()==0:
                return cnt
        return -1

# time complexity: O(Q * N), where Q is the length of queries and N is the length of nums
# space complexity: O(N), where N is the length of nums since we use a set to store unique elements