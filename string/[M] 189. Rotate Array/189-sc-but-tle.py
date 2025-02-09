class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        while k > 0:
            last = nums[-1]
            tmp = nums[0]
            for i in range(len(nums)-1):
                l_tmp = nums[i+1] 
                nums[i+1] = tmp 
                tmp = l_tmp 
                
            nums[0] = last

            k -= 1

# time complexity: O(n*k)
# space complexity: O(1)

# TLE Solution