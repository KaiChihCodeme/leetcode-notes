class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        cur = max(weights)
        # calculate capacity from max(weights) with brute force
        while True:
            cnt = 0
            tmp = 0
            # iterate all weights and calculate the capacity in order of weights
            for i in weights:
                if cur - tmp - i > 0:
                    tmp += i
                elif cur - tmp - i == 0:
                    cnt += 1
                    tmp = 0
                else:
                    cnt += 1
                    tmp = i

            # post process
            if tmp > 0:
                cnt += 1

            if cnt <= days:
                return cur
            else:
                cur += 1
                
# time complexity: O(N^2)
# space complexity: O(1)