class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(g):
            # if goal is 0, we will have -1 which is not make sense
            if g < 0:
                return 0

            # use l and r with sliding window
            l = 0
            # current sum for the sliding window
            cur_sum = 0
            # total cnt
            res = 0

            # by iterate right index to scale the sliding window
            for r in range(len(nums)):
                # cur_sum need to add the new right index value
                cur_sum += nums[r]

                # check if cur_sum grater than g, we need to narrow down the slinding window by moving left index
                while cur_sum > g:
                    cur_sum -= nums[l]
                    l += 1

                # after the while loop, here must be cur_sum <= g, so add to result by adding sliding window size
                res += (r - l + 1)
            return res

        # e.g., if goal = 2
        # we will calculate the <= 2 - <= 1 will be =2
        return helper(goal) - helper(goal-1)

# time complexity: O(n)
# space complexity: O(1)