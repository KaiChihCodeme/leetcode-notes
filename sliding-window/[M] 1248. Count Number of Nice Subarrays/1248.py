class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        tmp_sum = 0
        l = 0
        f_odd = float('inf')
        ans = 0
        
        # move right index to sacle the sliding window
        for r in range(len(nums)):
            # find the odd number from right index
            if nums[r] % 2 == 1:
                # update the first index of odd number
                if f_odd > r:
                    f_odd = r
                # add tmp_sum for the odd number
                tmp_sum += 1

            # check if tmp_sum is greater than k, means we need to move left index to shrink the window
            while tmp_sum > k:
                # if the left index is odd, we need to decrease the tmp_sum
                if nums[l] % 2 ==1:
                    tmp_sum -= 1
                    # update the f_odd due to the left index is f_odd
                    for i in range(l+1, r+1):
                        if nums[i] % 2 == 1:
                            f_odd = i
                            break
                l += 1

            # if tmp_sum is equal to k, means we find a nice subarray
            # the number of nice subarray is the number of odd number from the left index to the first odd number
            if tmp_sum == k:
                ans += (f_odd - l + 1)


        return ans
                
# time complexity: O(n)
# space complexity: O(1)