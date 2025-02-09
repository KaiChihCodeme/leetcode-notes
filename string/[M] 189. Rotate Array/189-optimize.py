class Solution:
    def reverse (self, nums, i, j) : 
        li = i
        ri = j
        
        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp
            
            li += 1
            ri -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0 : 
            k += len(nums)
        
        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);

# time complexity: O(n)
# space complexity: O(1)
# reference: https://leetcode.com/problems/rotate-array/solutions/1730142/java-c-python-a-very-very-well-detailed-explanation