class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = dict()
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        boundary = len(nums) / 2
        for ind, cnt in m.items():
            if cnt >= boundary:
                return ind

# time complexity: O(n)
# space complexity: O(n)