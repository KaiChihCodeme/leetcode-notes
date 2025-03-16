class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Use binary search to search the minimum k by log(N)
        l, r = 0, len(queries)
        
        # if r cannot form zero array, we cannot find any
        if not self.can_form_zero_array(nums, queries, r):
            return -1

        while l <= r:
            m = l + (r - l) // 2
            if self.can_form_zero_array(nums, queries, m):
                r = m - 1
            else:
                l = m + 1

        return l


    def can_form_zero_array(self, nums, queries, k):
        n = len(nums)
        total_sum = 0
        difference_arr = [0] * (n+1)

        # this is tricky and hard to understand at first glance
        # use difference array to track the sum of values at each index
        # for example: [2,0,2] & [[0,2,1],[0,2,1],[1,1,3]] -> [1,1,1], [1,1,1], [0,3,0] -> [2,5,2]
        # final will get [2,3,-3,-2]. due to we finally get [2,2+3,2+3-3, 2+3-3-2] like above one
        # why minus? because in the next index, it will not +val, so -val we get the correct one in sum
        for query_index in range(k):
            start, end, val = queries[query_index]

            difference_arr[start] += val
            difference_arr[end+1] -= val

        # calculate sum and compare with each nums array
        for num_ind in range(n):
            total_sum += difference_arr[num_ind]

            # if sum smaller than nums, it means this k do not fit zero arry
            if total_sum < nums[num_ind]:
                return False
        return True
    
# time complexity: O(log(M)*(N+M))
# space complexity: O(N), where N is the length of nums since we use a difference array to store the differences