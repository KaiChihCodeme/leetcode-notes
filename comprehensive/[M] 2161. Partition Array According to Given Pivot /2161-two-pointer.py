class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, r = 0, len(nums)-1
        result = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] < pivot:
                result[l] = nums[i]
                l += 1
            
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > pivot:
                result[r] = nums[j]
                r -= 1

        while l <= r:
            result[l] = pivot
            l += 1

        return result
                
# time complexity: O(n)
# space complexity: O(n)